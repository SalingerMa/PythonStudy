# -*- coding: utf-8 -*-

def is_isbn_or_key(word):
    """
    判断搜索方式是isbn还是关键字

    isbn desc:

    1) isbn13: it's make up of 13 numbers from 0-9
    2) isbn10: it's make up of 10 number from 0-9 and some '-'
    """
    isbn_or_key = 'key'
    if len(word) == 13 and word.isdigit():
        isbn_or_key = 'isbn'
    short_word = word.replace('-', '')
    if '-' in short_word and len(short_word) == 10 and short_word.isdigit():
        isbn_or_key = 'isbn'

    return isbn_or_key