#!/usr/bin/env python3

from argparse import ArgumentParser

class WebLogHelper():
    """Provides functionality to filter a given webserver logfile based on a given IP address
        
    Note:
        This utility class works with common websever log formats where IP address logged as the first string
        of the log line and do not support log formats such as JSON or XML
    """
    def __init__(self, filter_ip, log_file):
        """Class constructor

        Args:
            filter_ip (str): IP address to filter the log
            log_file (str): relative or absolute path to the log file
        """
        self.filter_ip = filter_ip
        self.web_log_file = log_file

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