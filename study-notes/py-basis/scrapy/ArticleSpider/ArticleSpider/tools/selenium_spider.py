# -*- coding: utf-8 -*-

from scrapy import Selector

import time
from selenium import webdriver

# Optional argument, if not specified will search path.
driver = webdriver.Chrome(
    '/Users/zhushuangquan/Native Drive/GitHub/coderZsq.practice.data/study-notes/py-basis/scrapy/ArticleSpider/ArticleSpider/tools/chromedriver')
driver.get('http://www.google.com/xhtml')
time.sleep(5)  # Let the user actually see something!
search_box = driver.find_element_by_name('q')
search_box.send_keys('ChromeDriver')
search_box.submit()
time.sleep(5)  # Let the user actually see something!
driver.quit()

# t_selector = Selector(text=browser.page_source)
# t_selector.css('.tm-promo-price .tm-price::text').extract()

# browser.get('https://www.zhihu.com/#signin')
# import time
# time.sleep(10)
# browser.find_element_by_css_selector('.view-signin input[name="account"]').send_keys('18782902568')
# browser.find_element_by_css_selector('.view-signin input[name="password"]').send_keys('admin123')
# browser.find_element_by_css_selector('.view-signin button.sign-button').click()

