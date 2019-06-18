# -*- coding: utf-8 -*-
from flask import jsonify
from fisher import app

from heaper import is_isbn_or_key
from yushu_book import YuShuBook

@app.route('/book/search/<q>/<page>')
def search(q, page):
    """
    书籍搜索
    :param q: 普通关键字搜索，isbn
    :param page: 请求页数
    :return:
    """
    isbn_or_key = is_isbn_or_key(q)
    if isbn_or_key == 'isbn':
        result = YuShuBook.search_by_isbn(q)
    else:
        result = YuShuBook.search_by_keyword(q)
    return jsonify(result)
