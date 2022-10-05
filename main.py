#!/usr/bin/python3
# -*- coding: utf-8 -*-
import os
from configparser import RawConfigParser
from datetime import datetime

from mappsmusicplayer.config import __version__
from mappsmusicplayer.music_server import MusicServer
from mappsmusicplayer.tools import Colors
from mappsmusicplayer.tools import colorstring as c

inifile = 'config.ini'
musicserver = None  # type: MusicServer

# Start main program
banner = c("\n"
           "\tMelonMusicPlayer made by Melle Dijkstra © " + str(datetime.now().year) + "\n"
                                                                                       "\tVersion: " + __version__ + "\n",
           Colors.BLUE)

if __name__ == '__main__':
    # Check if program is run with root privileges, which is needed for socket communication
    try:
        print(banner)

        # Get configuration for the application
        config = RawConfigParser(defaults={})
        if os.path.exists(inifile):
            config.read_file(open(inifile))
        else:
            print(c('configuration file (' + inifile + ') does not exist', Colors.WARNING))

        musicserver = MusicServer(config)
        # This method will start the music_server and wait for anyone to connect
        musicserver.serve()
    except KeyboardInterrupt as e:
        print(c("Aborting MelonMusicPlayer...", Colors.BOLD))
        musicserver.shutdown()

musicserver.shutdown()
