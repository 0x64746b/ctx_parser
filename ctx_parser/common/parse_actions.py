# coding: utf-8

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals


# Custom parse actions
def num(tokens):
    """Convert a list of an optional sign and an integer value into an int."""
    flattened = ''.join(tokens)
    return int(flattened)


def convert_to_int(tokens):
    return num(tokens[0])
