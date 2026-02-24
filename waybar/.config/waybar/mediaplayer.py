#!/usr/bin/env python3
import argparse
import logging
import sys
import signal
import gi
import json
gi.require_version('Playerctl', '2.0')
from gi.repository import Playerctl, GLib

logger = logging.getLogger(__name__)

def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('--player')
    return parser.parse_args()

def on_metadata(player, metadata, manager):
    keys = metadata.keys()
    if 'xesam:artist' in keys and 'xesam:title' in keys:
        artist = metadata['xesam:artist'][0]
        title = metadata['xesam:title']
        print(json.dumps({'text': f"{artist} - {title}", 'class': 'custom-spotify', 'alt': 'spotify'}))
        sys.stdout.flush()

def on_play(player, status, manager):
    on_metadata(player, player.props.metadata, manager)

def on_name_appeared(manager, name):
    init_player(name)

def init_player(name):
    player = Playerctl.Player.new_from_name(name)
    player.connect('metadata', on_metadata, manager)
    player.connect('playback-status', on_play, manager)
    on_metadata(player, player.props.metadata, manager)

manager = Playerctl.PlayerManager()
manager.connect('name-appeared', on_name_appeared)

for name in manager.props.player_names:
    init_player(name)

loop = GLib.MainLoop()
loop.run()
