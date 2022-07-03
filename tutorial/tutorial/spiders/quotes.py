import scrapy

from ..items import QuoteItem


class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        # quotes = response.xpath('//div[@class="quote"]')
        quotes = response.css('.quote')

        for quote in quotes:
            item = QuoteItem()
            item['text'] = quote.css('.text::text').extract_first()  # 内容
            item['author'] = quote.css('.author::text ').extract_first()  # 作者
            item['tags'] = quote.css('.tags .tag::text').extract()  # 标签
            yield item

        next = response.css('.pager .next a::attr("href")').extract_first()
        url = response.urljoin(next)
        yield scrapy.Request(url=url, callback=self.parse)