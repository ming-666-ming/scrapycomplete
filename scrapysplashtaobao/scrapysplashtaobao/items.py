# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field


class TaobaoItems(Item):

    collection = 'productstaobao'

    image = Field()
    price = Field()
    dela = Field()
    location = Field()
    title = Field()
    shop = Field()
