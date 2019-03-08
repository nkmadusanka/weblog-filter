#!/usr/bin/env python3

from unittest import TestCase, main
# from weblog_helper import setup_commandline_options, WebLogHelper, LogFileParameterException
import weblog_helper
from argparse import ArgumentParser
import ipaddress
from unittest.mock import patch, call
import builtins

weblog_helper.print = lambda *args,**kwargs:builtins.print(*args,**kwargs)

class WebLogHelperTest(TestCase):
    def test_setup_commandline_options_returns_argument_parser(self):
        self.assertIsInstance(weblog_helper.setup_commandline_options(), ArgumentParser)

    def test_init_set_filter_ip_when_ip_is_valid(self):
        helper = weblog_helper.WebLogHelper('192.168.0.1', 'my-log-file.log')
        self.assertListEqual(helper.filter_ip_list, ['192.168.0.1'])

    def test_init_set_filter_ip_when_cidr_is_valid(self):
        helper = weblog_helper.WebLogHelper('192.168.1.0/30', 'my-log-file.log')
        self.assertListEqual(helper.filter_ip_list, ['192.168.1.0', '192.168.1.1', '192.168.1.2', '192.168.1.3'])

    def test_init_raise_exception_when_ip_is_just_a_string(self):
        self.assertRaises(ValueError, weblog_helper.WebLogHelper, 'just-a-string', 'my-log-file.log')

    def test_init_raise_exception_when_ip_is_invalid(self):
        self.assertRaises(ValueError, weblog_helper.WebLogHelper, '192.168.0', 'my-log-file.log')

    def test_init_raise_exception_when_ip_is_None(self):
        self.assertRaises(ValueError, weblog_helper.WebLogHelper, None, 'my-log-file.log')

    def test_init_raise_exception_when_cidr_is_invalid(self):
        self.assertRaises(ValueError, weblog_helper.WebLogHelper, '192.168.34.56/12', 'my-log-file.log')

    def test_init_set_log_file_string(self):
        helper = weblog_helper.WebLogHelper('192.168.0.1', 'my-log-file.log')
        self.assertEqual(helper.web_log_file, 'my-log-file.log')

    def test_init_set_log_file_number_string(self):
        helper = weblog_helper.WebLogHelper('192.168.0.1', 12345)
        self.assertEqual(helper.web_log_file, 12345)

    def test_init_raise_exception_when_log_file_is_None(self):
        self.assertRaises(weblog_helper.LogFileParameterException, weblog_helper.WebLogHelper, '192.168.0.1', None)

    def test_init_raise_exception_when_log_file_is_empty(self):
        self.assertRaises(weblog_helper.LogFileParameterException, weblog_helper.WebLogHelper, '192.168.0.1', '')

    @patch("weblog_helper.print", autospec=True)
    def test_run_filter_filter_log_by_ip(self, print_mock):
        helper = weblog_helper.WebLogHelper('31.184.238.128', './test-data/small.log')
        helper.run_filter()
        print_mock.assert_called_with('31.184.238.128 - - [02/Jun/2015:17:00:12 -0700] "GET /logs/access.log HTTP/1.1" 200 2145998\n', end='')
    
    @patch("weblog_helper.print", autospec=True)
    def test_run_filter_filter_log_by_ip(self, print_mock):
        helper = weblog_helper.WebLogHelper('178.93.28.59', './test-data/small.log')
        print_calls = [ call('178.93.28.59 - - [02/Jun/2015:17:06:06 -0700] "GET /logs/access_150122.log HTTP/1.1" 200 3240056\n', end=''),
                    call('178.93.28.59 - - [02/Jun/2015:17:06:09 -0700] "GET /logs/access_150122.log HTTP/1.1" 200 3240056\n', end=''),
                    call('178.93.28.59 - - [02/Jun/2015:17:06:10 -0700] "GET /logs/access_150122.log HTTP/1.1" 200 3240056\n', end=''),
                    call('178.93.28.59 - - [02/Jun/2015:17:06:11 -0700] "GET /logs/access_150122.log HTTP/1.1" 200 720088\n', end=''),
                    call('178.93.28.59 - - [02/Jun/2015:17:06:11 -0700] "GET /logs/access_150122.log HTTP/1.1" 200 3240056\n', end='')]
        helper.run_filter()
        print_mock.assert_has_calls(print_calls, any_order=False)
    
    @patch("weblog_helper.print", autospec=True)
    def test_run_filter_filter_log_by_cidr(self, print_mock):
        helper = weblog_helper.WebLogHelper('180.76.15.0/24', './test-data/small.log')
        print_calls = [ call('180.76.15.135 - - [02/Jun/2015:17:05:23 -0700] "GET /logs/access_140730.log HTTP/1.1" 200 979626\n', end=''),
                    call('180.76.15.137 - - [02/Jun/2015:17:05:28 -0700] "GET /logs/access_140730.log HTTP/1.1" 200 7849856\n', end='')]
        helper.run_filter()
        print_mock.assert_has_calls(print_calls, any_order=False)

if __name__ == '__main__':
    main()
