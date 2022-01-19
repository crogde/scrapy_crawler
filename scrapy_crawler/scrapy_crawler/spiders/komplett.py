import scrapy
from ..items import Product
from scrapy.loader import ItemLoader


class KomplettSpider(scrapy.Spider):
    name = 'komplett'
    allowed_domains = ['komplett.no/']
    start_urls = ['https://www.komplett.no/category/30000/tv-lyd-bilde/tv-video?nlevel=10719%C2%A730000&hits=500']

    def parse(self, response):
        
        for p in response.css('div.product-list-item'):
            
            prod = ItemLoader(item=Product(), selector=p)

            prod.add_css('title', 'img.product-image::attr(title)')
            prod.add_css('price','span.product-price-now')
            prod.add_css('link', 'a.product-link::attr(href)')

            yield prod.load_item()      