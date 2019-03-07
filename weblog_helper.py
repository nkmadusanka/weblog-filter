#!/usr/bin/env python3

from argparse import ArgumentParser

def setup_commandline_options():
    """Setup CLI switches for the weblog_helper script

    Returns:
        ArgumentParser instance
    """
    argument_parser = ArgumentParser(description="Filter a web log based on an given IP address.")
    argument_parser._action_groups.pop()  # argparse treat -- switches as optional, simple hack to make them required args
    required = argument_parser.add_argument_group("Required Arguments")
    required.add_argument("--ip", help="Valid IP address")
    required.add_argument("--log", help="Log file to analize")
    return argument_parser

if __name__ == '__main__':
    arg_parser = setup_commandline_options()
    args = arg_parser.parse_args()
    print(args)