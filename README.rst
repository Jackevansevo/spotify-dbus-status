===================
Dbus-Spotify-Status
===================

.. class:: no-web

    .. image:: https://raw.githubusercontent.com/Jackevansevo/spotify-dbus-status/master/screenshot.png
        :alt: i3blocks screenshot
        :width: 100%
        :align: center


Requirements
============

Requires python3 dbus package::

    λ sudo apt install python3-dbus


Installation
============

Install with pip::

    λ pip install spotify-dbus-status

Usage
=====

Enter `spotify-dbus-status` at the command line::

    λ spotify-dbus-status
    Flying Lotus - Zodiac Shit - Cosmogramma


The (--all) flag is implicit if nothing is specified::
  
    λ spotify-dbus-status --all                                           
    Flying Lotus - Zodiac Shit - Cosmogramma


Get specific data::

    λ spotify-dbus-status --album
    Cosmogramma

    λ spotify-dbus-status --artist 
    Flying Lotus

    λ spotify-dbus-status --song  
    Zodiac Shit


Ordered output::

    λ spotify-dbus-status --song --artist        
    Zodiac Shit - Flying Lotus


Custom seperator::

    λ spotify-dbus-status --song --album --sep=", "
    Zodiac Shit, Cosmogramma


Provide Template string::

    λ spotify-dbus-status --template="[Artist: {artist} | Album: {album}]"
    [Artist: Flying Lotus | Album: Cosmogramma]


As JSON::

    λ spotify-dbus-status --format=json            
    {"album": "Cosmogramma", "artist": "Flying Lotus", "song": "Zodiac Shit"}


You can then parse by piping into jq::

    λ spotify-dbus-status --format=json | jq -r '.artist + " - " + .song'
    Flying Lotus - Zodiac Shit


i3blocks Integration
====================

Add the following section (or similar) to you i3blocks.conf::

    [spotify]
    label= 
    command=spotify-dbus-status --template="{artist} - {song}"
    interval=2
    signal=10
    color=#24CF5F

Contributor Thanks
==================

- francois-contat_ : fixing utf-8 support

.. _francois-contat: https://github.com/francois-contat
