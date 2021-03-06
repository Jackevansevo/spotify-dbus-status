import six
import json
from argparse import ArgumentParser
from sys import argv, stdout

import pkg_resources

import dbus

session_bus = dbus.SessionBus()

bus_data = ("org.mpris.MediaPlayer2.spotify", "/org/mpris/MediaPlayer2")
spotify_bus = session_bus.get_object(*bus_data)

interface = dbus.Interface(spotify_bus, "org.freedesktop.DBus.Properties")

if six.PY3:
    metadata = interface.Get("org.mpris.MediaPlayer2.Player", "Metadata")
else:
    # Fallback to allow for UTF-8 strings in Python2
    metadata = interface.Get("org.mpris.MediaPlayer2.Player", "Metadata", utf8_strings=True)



def main():

    formats = ("json", "str")
    parser = ArgumentParser()
    parser.add_argument(
        "-v", "--version", action="store_true", help="show version"
    )
    parser.add_argument("--all", action="store_true")
    parser.add_argument("--artist", action="store_true")
    parser.add_argument("--song", action="store_true")
    parser.add_argument("--album", action="store_true")
    parser.add_argument("--format", default="str", choices=formats)
    parser.add_argument("--sep", default=" - ")
    parser.add_argument("--template")

    args = parser.parse_args()

    if args.version:
        version = pkg_resources.require("spotify-dbus-status")[0].version
        print(version)
        return

    data_flags = ("artist", "song", "album")

    opts = dict()

    # Introspect argparse to get data_flags flags
    for action in parser._actions:
        if action.dest in data_flags:
            for option in action.option_strings:
                opts[option] = action.dest

    # Get the order in which flags were passed
    ordered = tuple(filter(None, (opts.get(arg) for arg in argv[1:])))
    data_flags = ordered or data_flags

    # If no data flags are passed default to all
    if args.all or not any(getattr(args, flag) for flag in data_flags):
        for flag in data_flags:
            setattr(args, flag, True)

    if args.template is None:

        # Find out which data values artist/song/album were present
        template_strings = (flag for flag in data_flags if getattr(args, flag))

        # Create a template string "{artist} {song} ..."
        args.template = args.sep.join(
            ["{" + flag + "}" for flag in template_strings]
        )

    data = dict()

    if args.artist:
        artist_data = metadata.get("xesam:albumArtist")
        data["artist"] = next(iter(artist_data))

    if args.song:
        data["song"] = metadata.get("xesam:title")

    if args.album:
        data["album"] = metadata.get("xesam:album")

    formatters = {
        "json": lambda d: stdout.write(json.dumps(d, ensure_ascii=False)),
        "str": lambda d: stdout.write(args.template.format(**d)),
    }

    formatters.get(args.format)(data)


if __name__ == "__main__":
    main()
