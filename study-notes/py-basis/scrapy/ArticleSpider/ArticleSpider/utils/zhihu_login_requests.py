# -*- coding: utf-8 -*-

import requests

try:
    import cookielib
except:
    import http.cookiejar as cookielib

import re

session = requests.session()
session.cookies = cookielib.LWPCookieJar(filename='cookies.txt')

try:
    session.cookies.load(ignore_discard=True)
except:
    print('cookie未能加载')

agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
headers = {
    'HOST' : 'www.zhihu.com',
    'Referer' : 'https://www.zhihu.com',
    'User-Agent' : agent
}

def is_login():
    # 通过个人中心页面返回状态码来判断是否为登录状态
    index_url = 'https://www.zhihu.com/inbox'
    response = session.get(index_url, headers=headers, allow_redirects=False)
    if response.status_code != 200:
        return False
    else:
        return True

def get_xsrf():
    # 获取xsrf_code
    response = session.get('https://www.zhihu.com', headers=headers)
    match_obj = re.match('.*name="_xsrf" value="(.*?)"', response.text)
    if match_obj:
        return (match_obj.group(1))
    else:
        return ''

def get_index():
    response = session.get('https://www.zhihu.com', headers=headers)
    with open('index_page.html', 'wb') as f:
        f.write(response.text.encode('utf-8'))
    print('ok')

def zhihu_login(account, password):
    # 知乎登录
    if re.match('1\d{10}', account):
        print('手机号码登录')
        post_url = 'https://www.zhihu.com/login/phone_num'
        post_data = {
            '_xsrf': get_xsrf(),
            'phone_num' : account,
            'password' : password
        }
    else:
        if '@' in account:
            # 判断用户名是否为邮箱
            print('邮箱方式登录')
            post_url = 'https://www.zhihu.com/login/email'
            post_data = {
                '_xsrf': get_xsrf(),
                'email': account,
                'password': password
            }
    response = session.post(post_url, data=post_data, headers=headers)
    session.cookies.save()

zhihu_login('18782902568', 'admin123')
print(is_login())