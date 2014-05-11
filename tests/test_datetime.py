# coding: utf-8

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from datetime import datetime
import unittest

from ctx_parser import date_time


class TestTheDateTimeModule(unittest.TestCase):

    def test_can_parse_timestamps(self):
        # setup test data
        test_timestamp = 1399846525

        test_element = '"{}"'.format(test_timestamp)

        # test parsing of timestamp
        parsed_elements = date_time.TIMESTAMP.parseString(test_element)

        # check result
        self.assertEqual(
            parsed_elements[0],
            datetime.fromtimestamp(test_timestamp)
        )

    def test_can_parse_set_utc_flags(self):
        # setup test data
        test_bit = 1
        test_flag = 'int inUtc="{}"'.format(test_bit)

        # test parsing of flag
        parsed_elements = date_time.UTC_FLAG.parseString(test_flag)

        # check result
        self.assertEqual(parsed_elements.inUtc, True)

    def test_can_parse_unset_utc_flags(self):
        # setup test data
        test_bit = 0
        test_flag = 'int inUtc="{}"'.format(test_bit)

        # test parsing of flag
        parsed_elements = date_time.UTC_FLAG.parseString(test_flag)

        # check result
        self.assertEqual(parsed_elements.inUtc, False)
