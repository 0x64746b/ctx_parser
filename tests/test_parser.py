# coding: utf-8

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from datetime import datetime
import unittest

from six import string_types

from ctx_parser import parser


class TestTheParser(unittest.TestCase):

    def test_can_parse_lists(self):
        # setup test data
        test_string_1 = 'test_string_1'
        test_string_2 = 'test_string_2'

        test_list = """
          testElementList {
            testElement {
                char oneValue="%(first_value)s"
            } #testElement

            testElement {
                char anotherValue="%(second_value)s"
            } #testElement
          } #testElementList
        """ % {
            'first_value': test_string_1,
            'second_value': test_string_2,
        }

        # test parsing of list
        parsed_elements = parser.LIST.parseString(test_list)

        # check result
        self.assertEqual(
            parsed_elements.testElementList[0].oneValue,
            test_string_1
        )
        self.assertIsInstance(
            parsed_elements.testElementList[0].oneValue,
            string_types
        )

        self.assertEqual(
            parsed_elements.testElementList[1].anotherValue,
            test_string_2
        )
        self.assertIsInstance(
            parsed_elements.testElementList[1].anotherValue,
            string_types
        )

    def test_can_parse_composed_elements_containing_lists(self):
        # setup test data
        test_string_1 = 'test_string_1'
        test_string_2 = 'test_string_2'
        test_string_3 = 'test_string_3'

        test_element = """
          testElement {
            subElementList {
              subElement {
                char oneValue="%(first_value)s"
              }

              subElement {
                char anotherValue="%(second_value)s"
              }
            } #subElementList

            anotherElementList {
              anotherElement {
                char differentValue="%(third_value)s"
              }
            } #anotherList
          } #testElement
        """ % {
            'first_value': test_string_1,
            'second_value': test_string_2,
            'third_value': test_string_3,
        }

        # test parsing of composed element containing a list
        parsed_element = parser.COMPOSED_ELEMENT.parseString(test_element)

        # check result
        self.assertEqual(
            parsed_element.testElement.subElementList[0].oneValue,
            test_string_1
        )
        self.assertIsInstance(
            parsed_element.testElement.subElementList[0].oneValue,
            string_types
        )

        self.assertEqual(
            parsed_element.testElement.subElementList[1].anotherValue,
            test_string_2
        )
        self.assertIsInstance(
            parsed_element.testElement.subElementList[1].anotherValue,
            string_types
        )

        self.assertEqual(
            parsed_element.testElement.anotherElementList[0].differentValue,
            test_string_3
        )
        self.assertIsInstance(
            parsed_element.testElement.subElementList[0].differentValue,
            string_types
        )

    def test_can_parse_composed_elements_containing_composed_elements(self):
        # setup test data
        test_string_1 = 'test_string_1'
        test_string_2 = 'test_string_2'

        test_element = """
          testElement {
            subElement {
              char subValue="%(first_value)s"
            }

            anotherElement {
              char anotherValue="%(second_value)s"
            }
          } #testElement
        """ % {
            'first_value': test_string_1,
            'second_value': test_string_2,
        }

        # test parsing of nested composed elements
        parsed_element = parser.COMPOSED_ELEMENT.parseString(test_element)

        # check result
        self.assertEqual(
            parsed_element.testElement.subElement.subValue,
            test_string_1
        )
        self.assertIsInstance(
            parsed_element.testElement.subElement.subValue,
            string_types
        )

        self.assertEqual(
            parsed_element.testElement.anotherElement.anotherValue,
            test_string_2
        )
        self.assertIsInstance(
            parsed_element.testElement.anotherElement.anotherValue,
            string_types
        )

    def test_can_parse_composed_elements_containing_datetimes(self):
        # setup test data
        test_date_1 = datetime(2014, 5, 4, 20, 15, 45)
        test_date_2 = datetime(2014, 5, 4, 22, 40, 55)

        test_element = """
          testElement {
            testDate {
              date {
                int day="%(day_1)s"
                int month="%(month_1)s"
                int year="%(year_1)s"
              } #date

              int inUtc="1"

              time {
                int hour="%(hour_1)s"
                int min="%(minute_1)s"
                int sec="%(second_1)s"
              } #time
            } #testDate

            anotherDate {
              date {
                int day="%(day_2)s"
                int month="%(month_2)s"
                int year="%(year_2)s"
              } #date

              int inUtc="1"

              time {
                int hour="%(hour_2)s"
                int min="%(minute_2)s"
                int sec="%(second_2)s"
              } #time
            } #testDate
          } #testElement
        """ % {
            'year_1': test_date_1.year,
            'month_1': test_date_1.month,
            'day_1': test_date_1.day,
            'hour_1': test_date_1.hour,
            'minute_1': test_date_1.minute,
            'second_1': test_date_1.second,

            'year_2': test_date_2.year,
            'month_2': test_date_2.month,
            'day_2': test_date_2.day,
            'hour_2': test_date_2.hour,
            'minute_2': test_date_2.minute,
            'second_2': test_date_2.second,
        }

        # check parsing of datetimes in composed elements
        parsed_element = parser.COMPOSED_ELEMENT.parseString(test_element)

        # check result
        self.assertEqual(parsed_element.testElement.testDate, test_date_1)
        self.assertEqual(parsed_element.testElement.anotherDate, test_date_2)
