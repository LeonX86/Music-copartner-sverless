#!/usr/bin/env python
# coding=utf-8
"""
"""
__author__ = 'Alisue <lambdalisue@hashnote.net>'
import os
import sys
from .conf import create_default_config
from .arguments import parse_arguments
from .notifier import call_and_notificate

def main(args=None):
    # use system arguments if args is not specified
    args = args or sys.argv

    # create default configparser
    config = create_default_config()

    # parse argument, args indicate the non optional arguments
    # which will be used to call external program
    args, opts = parse_arguments(args, config)

    if opts.setup:
        # run setup wizard
        from .wizard import setup_wizard
        setup_wizard(config)
    elif opts.check:
        # run check
        from .conf import get_user_config_filename
        call_and_notificate(['cat', get_user_config_filename()], opts)
    elif len(args) > 0:
        # call and notify user
        call_and_notificate(args, opts)

if __name__ == '__main__':
    main()
