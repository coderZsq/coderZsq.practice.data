# -*- coding: utf-8 -*-
import scrapy
import re
from scrapy.http import Request
from urllib import parse

class JobboleSpider(scrapy.Spider):
    name = 'jobbole'
    allowed_domains = ['blog.jobbole.com']
    start_urls = ['http://blog.jobbole.com/all-posts/']

    def parse(self, response):
        # 获取文章列表页中的文章url并交给解析函数进行具体字段的解析
        # 获取下一页的url并交给scrapy进行下载
        
        # 解析列表页中的所有文章url并交给scrapy下载后进行解析
        post_nodes = response.css('#archive .floated-thumb .post-thumb a')
        for post_node in post_nodes:
            image_url = post_node.css('img::attr(src)').extract_first('')
            print(image_url)
            post_url = post_node.css('::attr(href)').extract_first('')
            yield Request(url=parse.urljoin(response.url, post_url), meta={'front_image_url' : image_url}, callback=self.parse_detail)
        #提取下一页并交给scrapy进行下载
        next_url = response.css('.next.page-numbers::attr(href)').extract_first("")
        if next_url:
            yield Request(url=parse.urljoin(response.url, next_url), callback=self.parse)

    def parse_detail(self, response):
        # 提取文章的具体字段
        # XPATH
        # title = response.xpath('//*[@class="entry-header"]/h1/text()').extract()[0]
        # create_date = response.xpath('//p[@class="entry-meta-hide-on-mobile"]/text()').extract()[0].strip().replace(" ·", "")
        # praise_nums = int(response.xpath('//span[contains(@class, "vote-post-up")]/h10/text()').extract()[0])
        # fav_nums = response.xpath('//span[contains(@class, "bookmark-btn")]/text()').extract()[0]
        # match_re = re.match('.*?(\d+).*', fav_nums)
        # if match_re:
        #     fav_nums = int(match_re.group(1))
        # else:
        #     fav_nums = 0
        # comment_nums = response.xpath('//a[@href="#article-comment"]/span/text()').extract()[0]
        # match_re = re.match('.*?(\d+).*', comment_nums)
        # if match_re:
        #     comment_nums = int(match_re.group(1))
        # else:
        #     comment_nums = 0
        # content = response.xpath('//div[@class="entry"]').extract()[0]
        # tag_list = response.xpath('//p[@class="entry-meta-hide-on-mobile"]/a/text()').extract()
        # tag_list = [element for element in tag_list if not element.strip().endswith("评论")]
        # tags = ", ".join(tag_list)

        # CSS
        title = response.css('.entry-header h1::text').extract()
        create_date = response.css('p.entry-meta-hide-on-mobile::text').extract()[0].strip().replace(" ·", "")
        praise_nums = response.css('.vote-post-up h10::text').extract()[0]
        fav_nums = response.css('.bookmark-btn::text').extract()[0]
        match_re = re.match(".*?(\d+).*", fav_nums)
        if match_re:
            fav_nums = int(match_re.group(1))
        else:
            fav_nums = 0
        comment_nums = response.css('a[href="#article-comment"] span::text').extract()[0]
        match_re = re.match('.*?(\d+).*', comment_nums)
        if match_re:
            comment_nums = int(match_re.group(1))
        else:
            comment_nums = 0
        content = response.css('div.entry').extract()[0]
        tag_list = response.css('p.entry-meta-hide-on-mobile a::text').extract()
        tag_list = [element for element in tag_list if not element.strip().endswith("评论")]
        tags = ", ".join(tag_list)
        # print(title)
        # print(create_date)
        # print(praise_nums)
        # print(fav_nums)
        # print(comment_nums)
        # print(content)
        # print(tags)
        pass
