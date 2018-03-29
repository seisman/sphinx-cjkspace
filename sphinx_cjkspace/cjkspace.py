# -*- coding: utf-8 -*-
# Inspired by https://blog.csdn.net/ancale/article/details/27982553
from .utils import is_ascii, is_cjk, is_cjk_punctuation
from docutils.nodes import *


def setup(app):
    app.connect('doctree-resolved', process_chinese_paragraph)


def cjkspacing(text):
    '''Fix spacing issue related to newlines of CJK characters.

    This function tries its best to remove the annoying whitespaces between CJK
    characters due to newlines, while keeping everything else untouched.
    '''

    def _check_cases(current_line, previous_line):
        # something strange happens
        if len(current_line) == 0 or len(previous_line) == 0:
            return '\n'
        if not is_ascii(previous_line[-1]) and not is_ascii(current_line[0]):
            return ''
        elif is_cjk_punctuation(previous_line[-1]) and is_ascii(current_line[0]):
            return ''
        else:
            return '\n'

    # split input text to several lines
    lines = text.splitlines()
    if len(lines) <= 1:  # empty text or only one line. Do nothing.
        return text

    # join lines by `\n' to restore original input text
    text_out = lines[0]
    for i in range(1, len(lines)):  # start from 1
        seperator = _check_cases(lines[i], lines[i-1])
        text_out += seperator + lines[i]
    if text.endswith('\n'):
        text_out += '\n'

    return text_out


class ParagraphVisitor(NodeVisitor):
    def dispatch_visit(self, node):
        if isinstance(node, paragraph):
            for i in range(len(node.children)):
                if type(node[i]) == Text:
                    node[i] = Text(cjkspacing(node[i].astext()))


def process_chinese_paragraph(app, doctree, docname):
    pv = ParagraphVisitor(doctree)
    doctree.walk(pv)
