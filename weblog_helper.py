#!/usr/bin/env python3

from argparse import ArgumentParser
import ipaddress

class LogFileParameterException(BaseException):
    """Custom Exception to specifically indicate that given log file name is invalid."""
    def __init__(self, *args, **kwargs):
        return super().__init__(*args, **kwargs)

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
        self.convert_ip_to_list(filter_ip)
        self.set_log_file(log_file)

    def convert_ip_to_list(self, ip):
        self.filter_ip_list = [ipaddress.ip_address(ip)]

    def set_log_file(self, log_file):
        if log_file:
            self.web_log_file = log_file
        else:
            raise LogFileParameterException()

    def run_filter(self):
        with open(self.web_log_file) as log_content:
            for line in log_content:
                self.print_filtered_log_line(line)

    def print_filtered_log_line(self, log_line):
        ip_on_log = log_line.split(' ')[0]
        if ipaddress.ip_address(ip_on_log) in self.filter_ip_list:
            print(log_line, end='')

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
    try:
        log_filter = WebLogHelper(args.ip, args.log)
        log_filter.run_filter()
    except LogFileParameterException:
        print("Did you forgot to mention the log file?")
        arg_parser.print_usage()
    except ValueError:
        print("%s is not a valid IP address" % args.ip)
    except FileNotFoundError:
        print("Log file '%s' does not exist." % args.log)