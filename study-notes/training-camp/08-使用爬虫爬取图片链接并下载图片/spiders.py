from bs4 import BeautifulSoup
import os
import requests
import shutil

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

url = 'http://www.infoq.com/cn/presentations'


def download_jpg(image_url, image_localpath):
    response = requests.get(image_url, stream=True)
    if response.status_code == 200:
        with open(image_localpath, 'wb') as f:
            shutil.copyfileobj(response.raw, f)


# 取得演讲图片
def craw3(url):
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'lxml')
    for pic_href in soup.find_all('div', class_='news_type_video'):
        for pic in pic_href.find_all('img'):
            imgurl = pic.get('src')
            dir = os.path.abspath('.')
            filename = os.path.basename(imgurl)
            imgpath = os.path.join(dir, filename)
            print('开始下载 %s' % imgurl)
            download_jpg(imgurl, imgpath)


# craw3(url)

# 翻页
j = 0
for i in range(12, 37, 12):
    url = 'http://www.infoq.com/cn/presentations' + str(i)
    j += 1
    print('第 %d 页' % j)
    craw3(url)
