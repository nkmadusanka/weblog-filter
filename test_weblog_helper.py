#!/usr/bin/env python3

from unittest import TestCase
from weblog_helper import setup_commandline_options, WebLogHelper, LogFileParameterException
from argparse import ArgumentParser
import ipaddress

class WebLogHelperTest(TestCase):
    def test_setup_commandline_options_returns_argument_parser(self):
        self.assertIsInstance(setup_commandline_options(), ArgumentParser)

    def test_init_set_filter_ip_when_ip_is_valid(self):
        helper = WebLogHelper('192.168.0.1', 'my-log-file.log')
        self.assertListEqual(helper.filter_ip_list, ['192.168.0.1'])

    def test_init_set_filter_ip_when_cidr_is_valid(self):
        helper = WebLogHelper('192.168.1.0/30', 'my-log-file.log')
        self.assertListEqual(helper.filter_ip_list, ['192.168.1.0', '192.168.1.1', '192.168.1.2', '192.168.1.3'])

    def test_init_raise_exception_when_ip_is_just_a_string(self):
        self.assertRaises(ValueError, WebLogHelper, 'just-a-string', 'my-log-file.log')

    def test_init_raise_exception_when_ip_is_invalid(self):
        self.assertRaises(ValueError, WebLogHelper, '192.168.0', 'my-log-file.log')

    def test_init_raise_exception_when_ip_is_None(self):
        self.assertRaises(ValueError, WebLogHelper, None, 'my-log-file.log')

    def test_init_raise_exception_when_cidr_is_invalid(self):
        self.assertRaises(ValueError, WebLogHelper, '192.168.34.56/12', 'my-log-file.log')

    def test_init_set_log_file_string(self):
        helper = WebLogHelper('192.168.0.1', 'my-log-file.log')
        self.assertEqual(helper.web_log_file, 'my-log-file.log')

    def test_init_set_log_file_number_string(self):
        helper = WebLogHelper('192.168.0.1', 12345)
        self.assertEqual(helper.web_log_file, 12345)

    def test_init_raise_exception_when_log_file_is_None(self):
        self.assertRaises(LogFileParameterException, WebLogHelper, '192.168.0.1', None)

    def test_init_raise_exception_when_log_file_is_empty(self):
        self.assertRaises(LogFileParameterException, WebLogHelper, '192.168.0.1', '')
