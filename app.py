#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    main
    ~~~~

    Endpoint of robo.


    :copyright: (c) 2015 Shinya Ohyanagi, All rights reserved.
    :license: BSD, see LICENSE for more details.
"""
import os
import argparse
import logging
from robo.robot import Robot


def main(args=None):
    """Main.

    :param args: :class:`argparse` Args
    """
    logging.basicConfig(level=args.verbose, format=Robot.debug_log_format)
    logger = logging.getLogger('robo')

    options = {'cron': {'jobstore': 'redis'}}
    robot = Robot(name=args.name, logger=logger, **options)
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        'my', 'handlers')

    robot.register_default_handlers()
    robot.setup_handlers(path, 'my.handlers')
    robot.load_adapter(args.adapter)
    robot.run(args.adapter)


def parse_options():
    """Parse options. """
    description = 'Dead simple bot framework'
    parser = argparse.ArgumentParser(description=description, add_help=False)
    parser.add_argument('-a', '--adapter', default='shell')
    parser.add_argument('-u', '--name', default='robo')
    parser.add_argument('-vv', '--verbose', default=logging.INFO, nargs='?',
                        const=logging.DEBUG)

    args = parser.parse_args()

    return args


if __name__ == '__main__':
    args = parse_options()
    main(args)
