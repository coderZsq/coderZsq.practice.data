# -*- coding: utf-8 -*-
import scrapy
import re
import json

class ZhihuSpider(scrapy.Spider):
    name = 'zhihu'
    allowed_domains = ['www.zhihu.com']
    start_urls = ['http://www.zhihu.com/']

    headers = {
        'HOST': 'www.zhihu.com',
        'Referer': 'https://www.zhihu.com',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
    }

    def parse(self, response):
        pass

    def start_requests(self):
        return [scrapy.Request('https://www.zhihu.com/#signin', headers=self.headers, callback=self.login)]

    def login(self, response):
        response_text = response.text
        match_obj = re.match('.*name="_xsrf" value="(.*?)"',response_text, re.DOTALL)
        xsrf = ''
        print(match_obj)
        if match_obj:
            xsrf = (match_obj.group(1))
        if xsrf:
            post_url = 'https://www.zhihu.com/login/phone_num',
            post_data = {
                '_xsrf': xsrf,
                'phone_num': '18782902568',
                'password': 'admin123'
            }
            return [scrapy.FormRequest(
                url=post_url,
                formdata=post_data,
                headers=self.headers,
                callback=self.check_login
            )]

    def check_login(self, response):
        # 验证服务器的返回数据判断是否成功
        text_json = json.loads(response.text)
        print(text_json)
        if 'msg' in text_json and text_json['msg'] == '登录成功' :
            for url in self.start_urls:
                yield self.make_requests_from_url(url)
        pass

