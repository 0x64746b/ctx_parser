# coding: utf-8

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from pyparsing import (
    Dict,
    Forward,
    Group,
    Literal,
    Optional,
    ZeroOrMore,
)

from ctx_parser.common.nonterminal_symbols import (
    COMMENT,
    INT_VALUE,
    NAME,
    NUMBER,
    STR_VALUE,
)
from ctx_parser.common.parse_actions import num
from ctx_parser.common.terminal_symbols import (
    char,
    equals,
    int as int_,
    lcurly,
    quote,
    rcurly,
    time,
)
from ctx_parser.date_time import (
    DATETIME,
    TIMESTAMP,
)


# Custom parse actions
def parseDivision(tokens):
    dividend, divisor = tokens
    return num(dividend) / num(divisor)


# Terminal symbols
slash = Literal('%2F').suppress()

# Nonterminal symbols
LIST = Forward()
COMPOSED_ELEMENT = Forward()

DIVISION = quote + NUMBER + slash + NUMBER + quote
DIVISION.setParseAction(parseDivision)

SIMPLE_ELEMENT = Dict(
    Group(
        char + NAME + equals + DIVISION |
        char + NAME + equals + STR_VALUE |
        int_ + time + equals + TIMESTAMP |
        int_ + NAME + equals + INT_VALUE
    )
)

COMPOSED_ELEMENT << Dict(
    Group(
        NAME + lcurly +
        ZeroOrMore(LIST | DATETIME | COMPOSED_ELEMENT | SIMPLE_ELEMENT) +
        rcurly + Optional(COMMENT)
    )
)

LIST << Dict(
    Group(
        NAME + lcurly +
        ZeroOrMore(COMPOSED_ELEMENT) +
        rcurly + Optional(COMMENT)
    )
)
