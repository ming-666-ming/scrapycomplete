# coding:utf-8
"""
Name : rules.py.py
Author  : Mark
Contect : hongming666@outlook.com
Time    : 2022/6/10 10:31
Desc:
"""
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import Rule

rules = {
    'news': {
        Rule(LinkExtractor(allow='social\/.*\.html',
                           restrict_xpaths='//div[@id="js-news-media"]/ul[@class="item_list"]'),
             callback='parse_item'),

    }
}
