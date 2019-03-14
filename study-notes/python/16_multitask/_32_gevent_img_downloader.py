import urllib.request
import gevent
from gevent import monkey


def downloader(img_name, img_url):
    req = urllib.request.urlopen(img_url)
    img_content = req.read()
    with open(img_name, "wb") as f:
        f.write(img_content)


def main():
    gevent.joinall([
        gevent.spawn(downloader, "1.jpg", "http://rpic.douyucdn.cn/appCovers/2017/09/13/688928_20170913203807_big.jpg"),
        gevent.spawn(downloader, "2.jpg", "http://rpic.douyucdn.cn/appCovers/2017/07/22/2325374_20170722125724_big.jpg")
    ])


if __name__ == '__main__':
    main()


