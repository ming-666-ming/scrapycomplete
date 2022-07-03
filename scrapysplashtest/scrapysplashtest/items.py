# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field


class JdItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    collection = 'product'

    image = Field()
    price = Field()
    title = Field()
    shop = Field()
