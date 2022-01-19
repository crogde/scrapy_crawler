import scrapy


class KomplettSpider(scrapy.Spider):
    name = 'komplett'
    allowed_domains = ['komplett.no/']
    start_urls = ['http://komplett.no//']

    def parse(self, response):
        pass
