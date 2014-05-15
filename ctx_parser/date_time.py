# coding: utf-8

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import datetime

from pyparsing import (
    Dict,
    Group,
    Keyword,
    Optional,
)

from ctx_parser.common.terminal_symbols import (
    equals,
    int as int_,
    lcurly,
    quote,
    rcurly,
    time,
)
from ctx_parser.common.nonterminal_symbols import (
    COMMENT,
    NAME,
    POSITIVE_NUMBER,
    UINT_VALUE,
)


# Terminal symbols
date = Keyword('date')
day = Keyword('day')
month = Keyword('month')
year = Keyword('year')
hour = Keyword('hour')
min_ = Keyword('min')
sec = Keyword('sec')


# Custom parse actions
def parseTimestamp(tokens):
    timestamp = tokens[0]
    return datetime.datetime.fromtimestamp(int(timestamp))


def parseFlag(tokens):
    value = int(tokens[1])
    tokens[1] = bool(value)


def parseDate(tokens):
    args = tokens.asList()
    args.reverse()
    return datetime.date(*map(int, args))


def parseTime(tokens):
    return datetime.time(*map(int, tokens.asList()))


def parseDatetime(tokens):
    date_time = datetime.datetime.combine(*tokens[1:])
    tokens[1] = date_time
    del tokens[2]

TIMESTAMP = quote + POSITIVE_NUMBER + quote
TIMESTAMP.setParseAction(parseTimestamp)

UTC_FLAG = Dict(
    Group(
        (
            int_ + Keyword('inUtc') + equals + UINT_VALUE
        ).setParseAction(parseFlag)
    )
)

COMPOSED_DATE = (
    date.suppress() + lcurly +
    int_ + day.suppress() + equals + UINT_VALUE +
    int_ + month.suppress() + equals + UINT_VALUE +
    int_ + year.suppress() + equals + UINT_VALUE +
    rcurly + Optional(COMMENT)
)
COMPOSED_DATE.setParseAction(parseDate)

COMPOSED_TIME = (
    time.suppress() + lcurly +
    int_ + hour.suppress() + equals + UINT_VALUE +
    int_ + min_.suppress() + equals + UINT_VALUE +
    int_ + sec.suppress() + equals + UINT_VALUE +
    rcurly + Optional(COMMENT)
)
COMPOSED_TIME.setParseAction(parseTime)

DATETIME = Dict(
    Group(
        (
            NAME + lcurly +
            COMPOSED_DATE +
            UTC_FLAG.suppress() +
            COMPOSED_TIME +
            rcurly + Optional(COMMENT)
        ).setParseAction(parseDatetime)
    )
)
