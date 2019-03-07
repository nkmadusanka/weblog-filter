#!/usr/bin/env python3

from unittest import TestCase
from weblog_helper import setup_commandline_options
from argparse import ArgumentParser

class WebLogHelperTest(TestCase):
    def test_setup_commandline_options_returns_argument_parser(self):
        self.assertIsInstance(setup_commandline_options(), ArgumentParser)
