#!/usr/bin/python3
"""the text identation module"""


def text_indentation(text):
    """prints a text with 2 new lines
    after each of these characters: ., ? and :
    Args:
    text (str): the text to be idented
    """
    if type(text) is not str:
        raise TypeError('text must be a string')
    for i in text:
        print(i, end='')
        if i == '?' or i == '.' or i == ':':
            print('\n\n')
