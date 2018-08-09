# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
from movie.items import MovieItem, MovieItemLoader
from urllib import parse

class Top250Spider(scrapy.Spider):
    name = 'top250'
    allowed_domains = ['movie.douban.com']
    start_urls = ['http://movie.douban.com/top250']

    def parse(self, response):
        grid_view_items = response.css('.grid_view .item')
        for item in grid_view_items:
            url = item.css('a::attr(href)').extract_first('')
            yield Request(url=parse.urljoin(response.url, url), callback=self.parse_subject)
        next_url = response.css('.paginator .next a::attr(href)').extract_first('')
        if next_url:
            yield Request(url=parse.urljoin(response.url, next_url), callback=self.parse)

    def parse_subject(self, response):
        item_loader = MovieItemLoader(item=MovieItem(), response=response)
        item_loader.add_css('title', '.content h1 span::text')
        item_loader.add_css('year', '.content span.year::text')
        yield item_loader
