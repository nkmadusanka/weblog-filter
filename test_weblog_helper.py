#!/usr/bin/env python3

from unittest import TestCase
from weblog_helper import setup_commandline_options, WebLogHelper
from argparse import ArgumentParser

class WebLogHelperTest(TestCase):
    def test_setup_commandline_options_returns_argument_parser(self):
        self.assertIsInstance(setup_commandline_options(), ArgumentParser)

    def test_init_set_given_parameters(self):
        helper = WebLogHelper('myIPString', 'myLogFile')
        self.assertEqual(helper.filter_ip, 'myIPString')
        self.assertEqual(helper.web_log_file, 'myLogFile')
