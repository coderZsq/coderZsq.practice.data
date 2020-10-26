from bs4 import BeautifulSoup
import requests

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, sdch',
    'Accept-Language': 'zh-CN,zh;q=0.8',
    'Connection': 'close',
    'Cookie': '_gauges_unique_hour=1; _gauges_unique_day=1; _gauges_unique_month=1; _gauges_unique_year=1; _gauges_unique=1',
    'Referer': 'http://www.infoq.com',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36 Edg/85.0.564.60'
}

url = 'http://www.infoq.com/cn/news'


# 取得新闻标题
def craw2(url):
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'lxml')
    for title_href in soup.find_all('div', class_='news_type_block'):
        print([title.get('title')
               for title in title_href.find_all('a') if title.get('title')])


# craw2(url)

# 翻页
for i in range(15, 46, 15):
    url = 'http://www.infoq.com/cn/news/' + str(i)
    # print(url)
    craw2(url)