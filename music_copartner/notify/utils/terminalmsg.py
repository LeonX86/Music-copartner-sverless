# coding=utf-8
"""
"""
__author__ = 'Alisue <lambdalisue@hashnote.net>'
from .terminalsize import get_terminal_size

def termianlmsg(paragraphs, wallchar="*"):
    (width, height) = get_terminal_size()

    print(wallchar * width)
    print(wallchar, wallchar.rjust(width - len(wallchar) * 2 - 2))
