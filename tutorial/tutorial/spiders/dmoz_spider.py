import scrapy
from tutorial.items import DmozItem


class DmozSpider(scrapy.Spider):
    name = "dmoz"
    allowed_domains = ["dmoz.org"]

    start_urls = [
        'https://www.veryins.com/coco20002'
    ]

    # def start_requests(self):
    #     url = 'https://www.veryins.com'
    #     proxy = '127.0.0.0:12333'

    #     proxies = ""
    #     if url.startswith("http://"):
    #         proxies = "http://"+str(proxy)
    #     elif url.startswith("https://"):
    #         proxies = "https://"+str(proxy)
    #     # 注意这里面的meta={'proxy':proxies},一定要是proxy进行携带,
    #     # 其它的不行,后面的proxies一定 要是字符串,其它任何形式都不行
    #     yield scrapy.Request(url, callback=self.parse, meta={'proxy': proxies})

    def parse(self, response):
        for sel in response.xpath('//img/@data-original'):
            item = DmozItem()
            item['image_url'] = sel.extract()
            yield item
