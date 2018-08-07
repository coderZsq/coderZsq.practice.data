# -*- coding: utf-8 -*-

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

from scrapy import Selector
t_selector = Selector(text=driver.page_source)
t_selector.css('.tm-promo-price .tm-price::text').extract()

# 模拟登陆
driver.get('https://www.zhihu.com/#signin')
import time
time.sleep(10)
driver.find_element_by_css_selector('.view-signin input[name="account"]').send_keys('18782902568')
driver.find_element_by_css_selector('.view-signin input[name="password"]').send_keys('admin123')
driver.find_element_by_css_selector('.view-signin button.sign-button').click()

# 设置chromedriver不加载图片
chrome_opt = webdriver.ChromeOptions()
prefs = {'profile.managed_default_content_settings.images': 2}
chrome_opt.add_experimental_option('prefs', prefs)
driver = webdriver.Chrome(
    executable_path='/Users/zhushuangquan/Native Drive/GitHub/coderZsq.practice.data/study-notes/py-basis/scrapy/ArticleSpider/ArticleSpider/tools/chromedriver', chrome_options=chrome_opt)
driver.get('https://www.taobao.com')
print(driver.page_source)

# phantomjs, 无界面的浏览器, 多进程情况下phantomjs性能会下降很严重
driver = webdriver.PhantomJS(
    '/Users/zhushuangquan/Native Drive/GitHub/coderZsq.practice.data/study-notes/py-basis/scrapy/ArticleSpider/ArticleSpider/tools/phantomjs')
driver.get('https://www.taobao.com')
print(driver.page_source)
driver.quit()
