#!/usr/bin/env python

"""
mesh.py - Quick wireless mesh network setup
"""

from argparse import ArgumentParser, FileType
from configparser import ConfigParser
import logging
import os
import subprocess


DEFAULT_DEV = 'wlan0'
DEFAULT_ESSID = 'mesh'
DEFAULT_FREQ = '2412'
DEFAULT_CONFIG = '/etc/mesh.conf'

parser = ArgumentParser()
parser.description = __doc__
parser.add_argument('--dev', help='Device name (e.g. {})'.format(DEFAULT_DEV))
parser.add_argument('--essid', help='ESSID (e.g. {})'.format(DEFAULT_ESSID))
parser.add_argument('--config',
                    type=FileType(),
                    help='Config file (default is {})'.format(DEFAULT_CONFIG),
                    default=DEFAULT_CONFIG)
config = ConfigParser()


def main(dev=DEFAULT_DEV,
         essid=DEFAULT_ESSID,
         freq=DEFAULT_FREQ):
    subprocess.check_call(('ip', 'link', 'set', dev, 'down'))
    subprocess.check_call(('ip', 'link', 'set', dev, 'mtu', '1528'))
    subprocess.check_call(('iw', dev, 'set', 'type', 'ibss'))
    subprocess.check_call(('ip', 'link', 'set', dev, 'up'))
    subprocess.check_call(('iw', dev, 'ibss', 'join', 'mesh', freq))
    subprocess.check_call(('batctl', 'if', 'add', dev))
    subprocess.check_call(('avahi-autoipd', '-D', 'bat0'))


if __name__ == '__main__':
    args = parser.parse_args()
    config.readfp(args.config)
    config = config['config']
    main(dev=args.dev or config.get('Dev') or DEFAULT_DEV,
         essid=args.essid or config.get('ESSID') or DEFAULT_ESSID)
