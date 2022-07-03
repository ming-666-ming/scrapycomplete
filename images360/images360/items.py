# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from scrapy import Field, Item


class ImageItem(Item):
    # define the fields for your item here like:
    collection = table = 'images'
    id = Field()
    qhimg_url = Field()
    title = Field()
    qhimg_thumb = Field()