# coding: utf-8

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from pyparsing import (
    alphas,
    dblQuotedString,
    delimitedList,
    Group,
    Literal,
    nums,
    Optional,
    pythonStyleComment,
    removeQuotes,
    Word,
)

from ctx_parser.common.parse_actions import convert_to_int
from ctx_parser.common.terminal_symbols import quote


# Terminal symbols
minus = Literal('-')

# Nonterminal symbols
NAME = Word(alphas)
POSITIVE_NUMBER = Word(nums)
NUMBER = Group(Optional(minus) + POSITIVE_NUMBER)
STR_VALUE = delimitedList(dblQuotedString.setParseAction(removeQuotes))
INT_VALUE = quote + NUMBER + quote
INT_VALUE.setParseAction(convert_to_int)
UINT_VALUE = quote + POSITIVE_NUMBER + quote
COMMENT = pythonStyleComment.suppress()
