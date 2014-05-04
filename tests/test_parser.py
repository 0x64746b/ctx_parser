# coding: utf-8

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from six import string_types
import unittest

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
