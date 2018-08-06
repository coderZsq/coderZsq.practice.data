# -*- coding: utf-8 -*-

from selenium import webdriver
from scrapy import Selector

browser = webdriver.Firefox(
    executable_path='/Users/zhushuangquan/Native Drive/GitHub/coderZsq.practice.data/study-notes/py-basis/scrapy/ArticleSpider/ArticleSpider/tools/geckodriver')
browser.get('https://taobao.com')
print (browser.page_source)

t_selector = Selector(text=browser.page_source)
t_selector.css('.tm-promo-price .tm-price::text').extract()

browser.get('https://www.zhihu.com/#signin')
browser.find_element_by_css_selector('.view-signin input[name="account"]').send_keys('18782902568')
browser.find_element_by_css_selector('.view-signin input[name="password"]').send_keys('admin123')
browser.find_element_by_css_selector('.view-signin button.sign-button').click()

browser.quit()
