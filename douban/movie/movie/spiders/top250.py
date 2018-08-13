# -*- coding: utf-8 -*-
import scrapy
from movie.items import MovieItem, MovieItemLoader
from urllib import parse

from selenium import webdriver
from scrapy.xlib.pydispatch import dispatcher
from scrapy import signals

class Top250Spider(scrapy.Spider):
    name = 'top250'
    allowed_domains = ['movie.douban.com']
    start_urls = ['http://movie.douban.com/top250']

    headers = {
        "HOST": "movie.douban.com",
        "Referer": "http://movie.douban.com/",
        'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:51.0) Gecko/20100101 Firefox/51.0"
    }

    def __init__(self, *args, **kwargs):
        self.fail_urls = []
        self.driver = webdriver.Chrome(
            '/Users/zhushuangquan/Native Drive/GitHub/coderZsq.practice.data/douban/movie/movie/tools/chromedriver')
        super(Top250Spider, self).__init__(*args, **kwargs)
        dispatcher.connect(self.spider_closed, signal=signals.spider_closed)

    def spider_closed(self, spider):
        self.driver.quit()

    def parse(self, response):
        grid_view_items = response.css('.grid_view .item')
        for item in grid_view_items:
            url = item.css('a::attr(href)').extract_first('')
            yield scrapy.Request(url=parse.urljoin(response.url, url), headers=self.headers, callback=self.parse_subject)
        
        next_url = response.css('.paginator .next a::attr(href)').extract_first('')
        if next_url:
            yield scrapy.Request(url=parse.urljoin(response.url, next_url), headers=self.headers, callback=self.parse)

    def parse_subject(self, response):
        item_loader = MovieItemLoader(item=MovieItem(), response=response)
        item_loader.add_css('title', '#content h1 span::text')
        item_loader.add_css('year', '#content span.year::text')
        item_loader.add_css('rate', '#content .rating_num::text')
        item_loader.add_value('url', response.url)
        movie_item = item_loader.load_item();
        yield movie_item
