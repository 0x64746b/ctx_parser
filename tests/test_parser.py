# coding: utf-8

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import unittest

from ctx_parser import parser


class TestTheParser(unittest.TestCase):

    def test_can_parse_lists(self):
        # setup test data
        test_string = 'test_value'
        test_list = """
          testElementList {
            testElement {
                char string="%(string_value)s"
            } #testElement
          } #testElementList
          """ % {'string_value': test_string}

        # test parser
        parsed_elements = parser.LIST.parseString(test_list)

        # check result
        self.assertEqual(
            parsed_elements.testElementList[0].string,
            test_string
        )
