# -*- coding: utf-8 -*-
import re
from zhon import hanzi


def is_ascii(c):
    '''Check if an character is in ASCII.

    >>> is_ascii('E')
    True
    >>> is_ascii('?')
    True
    >>> is_ascii('中')
    False
    >>> is_ascii('？')
    False
    '''
    return ord(c) < 128


def is_cjk(c):
    '''Check if an character is in CJK.
    >>> is_cjk('中')
    True
    >>> is_cjk('？')
    False
    >>> is_cjk('E')
    False
    >>> is_cjk('?')
    False
    '''
    return True if re.match('[{}]'.format(hanzi.characters), c) else False


def is_cjk_punctuation(c):
    '''Check if an character is a CJK punctuation.
    >>> is_cjk_punctuation('？')
    True
    >>> is_cjk_punctuation('?')
    False
    >>> is_cjk_punctuation('中')
    False
    >>> is_cjk_punctuation('E')
    False
    '''
    return True if c in hanzi.punctuation else False


if __name__ == '__main__':
    import doctest
    doctest.testmod()
