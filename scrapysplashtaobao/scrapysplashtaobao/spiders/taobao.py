# from urllib.parse import quote
#
# import scrapy
# from scrapy_splash import SplashRequest
#
# from ..items import taobaoItem
#
#
# script = """
# function main(splash, args)
#   splash.images_enabled = false
#   assert(splash:go(args.url))
#   assert(splash:wait(args.wait))
#   js = string.format("document.querySelector('#mainsrp-pager > div > div > div > div.form > input').value=%d;
#   document.querySelector('#mainsrp-pager > div > div > div > div.form > span.btn.J_Submit').click()", args.page)
#   splash:evaljs(js)
#   assert(splash:wait(args.wait))
#   return splash:html()
# end
# """
# cookies = {
#     'cna': '//QkGrDN+0oCAbc++kJaG6Ng',
#     'miid': '4794244801425527935',
#     'tracknick': '\u5929\u5802\u5DF4\u5DF4\u5DF4',
#     'thw': 'cn',
#     'enc': '4NLALEZJYsNnTY/re5pvNEl5BwRKyiXFy/vj9af3yGxkE/Q5a8idnPfGQ091KYhyym189ZuX+X9VuCfy+BKvQQ==',
#     'UM_distinctid': '17f909e7b8b7d7-0377c9111a53ae-977173c-144000-17f909e7b8ce; t=9a45e34795640ce3bb9de37bd88fb5de',
#     'cookie2': '25e0148563ba10f25c8cd4f96e5471b3',
#     'xlly_s': '1',
#     'sgcookie': 'E1002A3GlpRmvn4xiMkY2rTol+PW8rqSE4Kgm/d5/K3nMnhJl9as88tzxcQV1Ok2MOMf1DZndKrX9sVTdNL8XKb/IpYPfd8v0qzldG12rAgRwkOIpYPfd8v0qzldG12rAgRwkOzuDsJjfiMhIvsLSvqc67x',
#     'uc3': 'nk2=r7kq1yA0YiHc1g==&lg2=VFC/uZ9ayeYq2g==&id2=UUBaC9zbzUliMA==&vt3=F8dCvCPQKKwqRRUd/bk=',
#     'csg': '3af4e72b',
#     'lgc': '\u5929\u5802\u5DF4\u5DF4\u5DF4',
#     'uc4': 'id4=0@U2LIB/ezzYp57MqelEI5aU76q00H&nk4=0@rVtQBgGBXtk85Z6v5YCJLWD1iHLC',
#     '_cc_': 'UIHiLt3xSw==',
#     'sg': '巴50',
#     '_nk_': '\u5929\u5802\u5DF4\u5DF4\u5DF4',
#     'cookie1': 'UNQxRA5829DX3c2FLWHYZoESWpUKTx0IMzYJv0rCV/Y=',
#     'mt': 'ci=104_1',
#     '_m_h5_tk': '4c8941e970ea8bfaee95bc450a28d29a_1656842624923',
#     '_m_h5_tk_enc': 'd08e9b0f25c127d6fcd16b663a96769a',
#     '_tb_token_': '558313e785331',
#     'uc1': 'cookie21=V32FPkk/gihF/S5nr3O5&cookie14=UoexNDOn67p03g==&cookie16=U+GCWk/74Mx5tgzv3dWpnhjPaQ==&existShop=false&pas=0&cookie15=W5iHLLyFOGW7aA==',
#     'JSESSIONID': '36FC9610FEAD0967720312D9B0DCC4C5',
#     'alitrackid': 'www.taobao.com',
#     'lastalitrackid': 'www.taobao.com',
#     'SL_G_WPT_TO': 'zh',
#     'SL_GWPT_Show_Hide_tmp': '1',
#     'SL_wptGlobTipTmp': '1',
#     'isg': 'BDw8SXGbcg5eREYM5kzr_aPgDdruNeBfiWSHqha9pydH4dxrPkbf72gTxQmZqRi3',
#     'tfstk': 'cUYdBy0otAD3CFC9gHnGztSl7ThGa6FdEW68yUgGdifjjlU4osYkoEevZD1P39hO.',
#     'l': 'eBSZfsBcL28-Pi0oBO5anurza77OfIRb4sPzaNbMiInca1-l9ptyONCHG6GvWdtjgtCL0etPUcfRbdLHR3f0iNAJz3h2q_rt3xvO.'
#
# }
#
# class TaobaoSpider(scrapy.Spider):
#     name = 'taobao'
#     allowed_domains = ['www.taobao.com']
#     base_url = 'http://s.taobao.com/search?q='
#
#     def start_requests(self):
#         for keyword in self.settings.get('KEY_WORDS'):
#             for page in range(1, self.settings.get('MAX_PAGE') + 1):
#                 self.logger.debug("正在爬取第{}页".format(page))
#                 url = self.base_url.format(keyword=quote(keyword))
#                 yield SplashRequest(url, callback=self.parse, endpoint='execute',
#                                     args={'lua_source': script, 'page': page, 'wait': 7, 'cookies':cookies})
#
#     def parse(self, response):
#         products = response.xpath('//*[@id="mainsrp-itemlist"]//div[@class="items"][1]//div[contain(@class, "item")]')
#         # self.logger.debug(products)
#         # self.logger.debug(products)
#
#         for product in products:
#             # self.logger.debug(product)
#             item = taobaoItem()
#             # "//*[@id="J_goodsList"]/ul/li[1]"
#
#             item['price'] = ''.join(product.xpath('.//div[contains(@class, "price")]//text()').extract()).strip()
#
#             item['image'] = ''.join(product.xpath('.//div[@class="pic]//img[contains(@class, "img")]/@data-src').extract()).strip()
#             item['title'] = ''.join(product.xpath('.//div[contains(@class, "title")]//text()').extract()).strip()
#             item['shop'] = ''.join(product.xpath('.//div[contains(@class, "shop")]//text()').extract()).strip()
#             item['deal'] = ''.join(product.xpath('.//div[contains(@class, "deal-cnt")]//text()').extract()).strip()
#             item['location'] = ''.join(product.xpath('.//div[contains(@class, "location")]//text()').extract()).strip()
#             yield item


from urllib.parse import quote

from scrapy import Spider
from scrapy_splash import SplashRequest

from ..items import TaobaoItems

script = """
function main(splash, args)
    headers={
    ["authority"] = "s.taobao.com",
    ["method"] = "GET",
    ["scheme"] = "https",
    ["accept"] = "*/*",
    ["accept-language"] = "zh-CN,zh;q=0.9",
    ["cookie"] = "",
    ["referer"] =  "referer: https://www.taobao.com/",
    ["sec-fetch-mode"] = "no-cors",
    ["upgrade-insecure-requests"] = 1,
    ["sec-fetch-user"] = "?1",
    ["sec-fetch-site"] = "same-origin",
    ["user-agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"
     }

  assert(splash:go{args.url,headers=headers})
  assert(splash:wait(args.wait))

  js = string.format("document.querySelector('#mainsrp-pager > div > div > div > div.form > input').value=%d;
  document.querySelector('#mainsrp-pager > div > div > div > div.form > span.btn.J_Submit').click()", args.page)
  splash:evaljs(js) 
  
  assert(splash:wait(args.wait))

  return splash:html()
end
"""


class TaoSpider(Spider):
    name = 'taobao'
    allowed_domains = ['www.taobao.com']
    base_url = 'https://s.taobao.com/search?&q='

    def start_requests(self):
        for keyword in self.settings.get('KEYWORDS'):
            for page in range(1, self.settings.get('MAX_PAGE') + 1):
                url = self.base_url + quote(keyword)
                yield SplashRequest(url, callback=self.parse, endpoint='execute',
                                    args={'lua_source': script, 'page': page, 'wait': 7})

    def parse(self, response):
        products = response.xpath('//div[@class="items"]/div')
        for product in products:
            item = TaobaoItems()
            item['shop'] = "".join(product.xpath('.//div[@class="shop"]/a//span/text()').extract()).strip()
            item['price'] = "".join(product.xpath('.//div[contains(@class, "price")]/strong/text()').extract()).strip()
            item['location'] = "".join(product.xpath('.//div[@class="location"]/text()').extract()).strip()
            item['deal'] = "".join(product.xpath('.//div[@class="deal-cnt"]/text()').extract()).strip()
            item['image'] = "".join(product.xpath('.//div[@class="pic"]//img/@src').extract()).strip()
            item['title'] = "".join(product.xpath('.//a[@class="J_ClickStat"]//text()').extract()).strip()
            yield item
