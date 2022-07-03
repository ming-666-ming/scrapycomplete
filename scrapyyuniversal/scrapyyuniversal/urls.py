# coding:utf-8
"""
Name : urls.py
Author  : Mark
Contect : hongming666@outlook.com
Time    : 2022/6/10 14:51
Desc:
"""


def china(start, end):
    for page in range(start, end+1):
        yield 'http://tech.china.com/articles/index_' + str(page) + '.html'