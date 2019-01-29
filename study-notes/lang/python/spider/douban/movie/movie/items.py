# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
import re
from scrapy.loader import ItemLoader
from scrapy.loader.processors import MapCompose, TakeFirst, Join

def get_year(value):
    match_re = re.match(".*?(\d+).*", value)
    if match_re:
        nums = int(match_re.group(1))
    else:
        nums = 0
    return nums

def get_rate(value):
    if value:
        return float(value)
    return 0

class MovieItemLoader(ItemLoader):
    default_output_processor = TakeFirst()

class MovieItem(scrapy.Item):
    title = scrapy.Field()
    year = scrapy.Field(
        input_processor=MapCompose(get_year),
    )
    rate = scrapy.Field(
        input_processor=MapCompose(get_rate),
    )
    url = scrapy.Field()

    def get_insert_sql(self):
        insert_sql = """
            insert into top250(title, year, rate, url)
            VALUES (%s, %s, %s, %s)
            ON DUPLICATE KEY UPDATE url=VALUES(url)
        """
        params = (
            self['title'], self['year'], self['rate'], self['url']
        )
        return insert_sql, params
