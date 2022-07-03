from scrapy import Request, Spider
from urllib.parse import quote

from ..items import JdItem


class JdSpider(Spider):
    name = 'jd'
    allowed_domains = ['jd.com']
    base_url = "https://search.jd.com/Search?keyword="

    def start_requests(self):
        for keyword in self.settings.get('KEY_WORDS'):
            for page in range(1, self.settings.get('MAX_PAGE')+1):
                url = self.base_url + quote(keyword)
                yield Request(url=url, callback=self.parse, meta={'page': page}, dont_filter=True)

    def parse(self, response):
        "/html/body/div[5]/div[2]/div[2]/div[1]/div/div[2]/ul/li[1]"
        products = response.xpath('//*[@id="J_goodsList"]/ul/li')
        # self.logger.debug(products)
        # self.logger.debug(products)

        for product in products:
            # self.logger.debug(product)
            item = JdItem()
            # "//*[@id="J_goodsList"]/ul/li[1]"
            ""
            item['image'] = ''.join(product.xpath('./div/div[1]/a/img/@src').extract()).strip()
            item['price'] = ''.join(product.xpath('./div/div[3]/strong/i/text()').extract()).strip()
            item['title'] = ''.join(product.xpath('./div/div[4]/a/em/text()').extract()).strip()
            item['shop'] = ''.join(product.xpath('./div/div[7]/span/a/text()').extract()).strip()
            yield item