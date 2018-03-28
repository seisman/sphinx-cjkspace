# -*- coding: utf-8 -*-
# Inspired by https://blog.csdn.net/ancale/article/details/27982553
from .utils import is_ascii, is_cjk, is_cjk_punctuation
from docutils.nodes import *


def setup(app):
    app.connect('doctree-resolved', process_chinese_paragraph)


def cjkspacing(text):
    '''Fix spacing issue related to newlines of CJK characters.

    The idea is to split input text by newlines and then join them to a string.
    '''
    # split input text into lines
    lines = text.splitlines()
    # deal with exceptions
    for i in range(1, len(lines)):  # start from 1
        # current line starts with ASCII and last line starts with hanzi
        try:
            if is_ascii(lines[i][0]) and not is_cjk_punctuation(lines[i-1][-1]):
                lines[i] = " " + lines[i]
            if is_ascii(lines[i][-1]) and not is_ascii(lines[i+1][0]):
                lines[i] = lines[i] + " "
        except IndexError:
            pass
    text = "".join(lines)
    return text


class ParagraphVisitor(NodeVisitor):
    def dispatch_visit(self, node):
        if isinstance(node, paragraph):
            for i in range(len(node.children)):
                if type(node[i]) == Text:
                    node[i] = Text(cjkspacing(node[i].astext()))


def process_chinese_paragraph(app, doctree, docname):
    pv = ParagraphVisitor(doctree)
    doctree.walk(pv)
