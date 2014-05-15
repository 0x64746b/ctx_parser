# coding: utf-8

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from datetime import date, datetime, time
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

    def test_can_parse_composed_dates(self):
        # setup test data
        test_date = date(2014, 5, 15)
        test_element = """
          date {
            int day="%(day)s"
            int month="%(month)s"
            int year="%(year)s"
          } #date
        """ % {
            'day': test_date.day,
            'month': test_date.month,
            'year': test_date.year,
        }

        # test parsing of composed date
        parsed_element = date_time.COMPOSED_DATE.parseString(test_element)

        # check result
        self.assertEqual(parsed_element[0], test_date)

    def test_can_parse_composed_times(self):
        # setup test data
        test_time = time(21, 50, 15)
        test_element = """
          time {
            int hour="%(hour)s"
            int min="%(min)s"
            int sec="%(sec)s"
          }
        """ % {
            'hour': test_time.hour,
            'min': test_time.minute,
            'sec': test_time.second,
        }

        # test parsing of composed time
        parsed_element = date_time.COMPOSED_TIME.parseString(test_element)

        # check result
        self.assertEqual(parsed_element[0], test_time)
