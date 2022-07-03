# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field


class NewsItem(Item):
    collection = 'news'
    title = Field()
    url = Field()
    text = Field()
    datetime = Field()
    source =Field()
    website = Field()