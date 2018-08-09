# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader import ItemLoader
from scrapy.loader.processors import MapCompose, TakeFirst, Join

class MovieItemLoader(ItemLoader):
    # 自定义itemloader
    default_output_processor = TakeFirst()

class MovieItem(scrapy.Item):
    title = scrapy.Field()
    year = scrapy.Field()
