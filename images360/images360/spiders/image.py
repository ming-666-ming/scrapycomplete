import json

from scrapy import Spider, Request
from urllib.parse import urlencode


from ..items import ImageItem


class ImageSpider(Spider):
    name = 'image'
    allowed_domains = ['image.so.com']
    start_urls = ['http://image.so.com/']

    def start_requests(self):
        offset = 30  # 数量
        params = {
            "ch": "beauty"
        }
        for page in range(1, self.settings.get('MAX_PAGE')):
            params["sn"] = offset * page
            url = "https://image.so.com/zjl?" + urlencode(params)
            yield Request(url=url, callback=self.parse)

    def parse(self, response):
        results = json.loads(response.text).get('list')
        for result in results:
            item = ImageItem()
            item['id'] = result.get('id')
            item['qhimg_url'] = result.get('qhimg_url')
            item['title'] = result.get('title')
            item['qhimg_thumb'] = result.get('qhimg_thumb')
            yield item



