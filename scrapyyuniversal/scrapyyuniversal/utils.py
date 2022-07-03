# coding:utf-8
"""
Name : utils.py
Author  : Mark
Contect : hongming666@outlook.com
Time    : 2022/6/10 10:13
Desc:
"""

from os.path import realpath, dirname
import json


def get_config(name):
    path = dirname(realpath(__file__)) + '/configs/' + name + '.json'
    print(path)
    with open(path, 'r', encoding='utf-8') as f:
        return json.loads(f.read())


