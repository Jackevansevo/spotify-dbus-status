from setuptools import setup

setup(
    name="spotify-dbus-status",
    version="0.1.2",
    url="https://github.com/Jackevansevo/spotify-dbus-status",

    author="Jack Evans",
    author_email="jack@evans.gb.net",

    description="Get the current spotify status from cmd line",
    long_description=open('README.rst').read(),

    license='MIT',

    py_modules=['status'],
    entry_points={
        'console_scripts': [
            'spotify-dbus-status=spotify_dbus_status:main'
        ]
    },

    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)
