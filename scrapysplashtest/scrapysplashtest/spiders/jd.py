from urllib.parse import quote

import scrapy
from scrapy_splash import SplashRequest

from ..items import JdItem

script = """
function main(splash, args)
  splash.images_enabled = false
  assert(splash:go(args.url))
  assert(splash:wait(args.wait))
  js = string.format("document.querySelector('#J_bottomPage > span.p-skip > input').value=%d;document.querySelector('#J_bottomPage > span.p-skip > a').click()", args.page)
  splash:evaljs(js)
  assert(splash:wait(args.wait))
  return splash:html()
end
"""


class JdSpider(scrapy.Spider):
    name = 'jd'
    allowed_domains = ['jd.com']
    base_url = 'https://search.jd.com/Search?keyword={keyword}'

    def start_requests(self):
        for keyword in self.settings.get('KEY_WORDS'):
            for page in range(1, self.settings.get('MAX_PAGE') + 1):
                self.logger.debug("正在爬取第{}页".format(page))
                url = self.base_url.format(keyword=quote(keyword))
                yield SplashRequest(url, callback=self.parse, endpoint='execute',
                                    args={'lua_source': script, 'page': page, 'wait': 7})

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
