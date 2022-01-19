# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from itemloaders.processors import MapCompose, TakeFirst, Join
from w3lib.html import remove_tags

def fixprice(text):
    return text.replace(u'\xa0', u' ')

class Product(scrapy.Item):
    # define the fields for your item here like:
    price = scrapy.Field(
        input_processor=MapCompose(remove_tags,fixprice),
    )
    title = scrapy.Field()
    
    link = scrapy.Field(
        output_processor=TakeFirst(),
        
        
    )