import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy.loader import ItemLoader
from scrapy.loader.processors import Join, TakeFirst, Compose

from ..items import NewsItem


class ChinaSpider(CrawlSpider):
    name = 'china'
    # allowed_domains = ['tech.china.com']
    start_urls = ['https://news.china.com/']

    rules = (

        Rule(LinkExtractor(allow='social\/.*\.html',restrict_xpaths='//div[@id="js-news-media"]/ul[@class="item_list"]'), callback='parse_item'),

        # Rule(LinkExtractor(restrict_xpaths='//*[@id="focus_next"]'))
    )

    def parse_item(self, response):
        loader = ChinaLoader(item=NewsItem(), response=response)
        loader.add_xpath('title', '//*[@id="js-info-flow"]/div[1]/h1/text()')
        loader.add_value('url', response.url)
        loader.add_xpath('text', '//*[@id="js_article_content"]//text()')
        loader.add_xpath('datetime', '//*[@id="js-info-flow"]/div[1]/div[2]/span[1]/text()', re='(\d+-\d+-+\d+\s\d+:\d+:\d+)')
        loader.add_xpath('source', '//*[@id="js-info-flow"]/div[1]/div[2]/span[2]/a/text()')
        loader.add_value('website', '中华网')
        # item = NewsItem()
        # item['title'] = response.xpath('//*[@id="js-info-flow"]/div[1]/h1/text()').extract_first()
        # item['url'] = response.url
        # item['text'] = ''.join(response.xpath('//*[@id="js_article_content"]//text()').extract()).strip()
        # item['datetime'] = response.xpath('//*[@id="js-info-flow"]/div[1]/div[2]/span[1]/text()').re_first('(\d+-\d+-+\d+\s\d+:\d+:\d+)')
        # item['source'] = response.xpath('//*[@id="js-info-flow"]/div[1]/div[2]/span[2]/a/text()').extract_first()
        # item['website'] = '中华网'
        return loader.load_item()


class NewsLoader(ItemLoader):
    default_output_processor = TakeFirst()


class ChinaLoader(NewsLoader):
    text_out = Compose(Join(), lambda s:s.strip())
    source_out = Compose(Join(), lambda s:s.strip())