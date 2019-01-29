# -*- coding: utf-8 -*-

from scrapy_redis.spiders import RedisSpider
from scrapy.http import Request
from urllib import parse

class JobboleSpider(RedisSpider):
    name = 'jobbole'
    allowed_domains = ['blog.jobbole.com']
    redis_key = 'jobbole:start_urls'

    def parse(self, response):
        # 获取文章列表页中的文章url并交给解析函数进行具体字段的解析
        # 获取下一页的url并交给scrapy进行下载

        # 解析列表页中的所有文章url并交给scrapy下载后进行解析
        post_nodes = response.css('#archive .floated-thumb .post-thumb a')
        for post_node in post_nodes:
            image_url = post_node.css('img::attr(src)').extract_first('')
            post_url = post_node.css('::attr(href)').extract_first('')
            yield Request(url=parse.urljoin(response.url, post_url), meta={'front_image_url': image_url}, callback=self.parse_detail)
        #提取下一页并交给scrapy进行下载
        next_url = response.css(
            '.next.page-numbers::attr(href)').extract_first("")
        if next_url:
            yield Request(url=parse.urljoin(response.url, next_url), callback=self.parse)

    def parse_detail(self, response):
        pass
