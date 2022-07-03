# coding:utf-8
"""
Name : loader.py
Author  : Mark
Contect : hongming666@outlook.com
Time    : 2022/6/10 15:19
Desc:
"""

from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst, Join, Compose


class NewsLoader(ItemLoader):
    default_output_processor = TakeFirst()


class ChinaLoader(NewsLoader):
    text_out = Compose(Join(), lambda s:s.strip())
    source_out = Compose(Join(), lambda s:s.strip())