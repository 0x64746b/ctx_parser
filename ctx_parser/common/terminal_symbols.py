# coding: utf-8

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from pyparsing import (
    Keyword,
    Literal,
)

# Terminal symbols
lcurly = Keyword('{').suppress()
rcurly = Keyword('}').suppress()
char = Keyword('char').suppress()
int = Keyword('int').suppress()
time = Keyword('time')
equals = Literal('=').suppress()
quote = Literal('"').suppress()
