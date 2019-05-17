# coding:utf-8

from flask import Flask, request, abort, render_template
import hashlib
import xmltodict
import time
import urllib2
import json

WECHAT_TOKEN = ""
WECHAT_APPID = ""
WECHAT_APPSECRET = ""

app = Flask(__name__)


@app.route("/wechat8000", methods=['GET', 'POST'])
def wechat():
    signature = request.args.get("signature")
    timestamp = request.args.get("timestamp")
    nonce = request.args.get("nonce")

    if not all([signature, timestamp, nonce]):
        abort(400)
    li = [WECHAT_TOKEN, timestamp, nonce]
    li.sort()
    tmp_str = "".join(li)
    sign = hashlib.sha1(tmp_str).hexdigest()
    if signature != sign:
        abort(403)
    else:
        if request.method == 'GET':
            echostr = request.args.get('echostr')
            if not echostr:
                abort(400)
            return echostr
        elif request.method == 'POST':
            xml_str = request.data
            if not xml_str:
                abort(400)
            xml_dict = xmltodict.parse(xml_str)
            xml_dict = xml_dict.get('xml')
            msg_type = xml_dict.get('MsgType')
            if msg_type == 'text':
                resp_dict = {
                    'xml': {
                        'ToUserName': xml_dict.get('FromUserName'),
                        'FromUserName': xml_dict.get('ToUserName'),
                        'CreateTime': int(time.time()),
                        'MsgType': 'text',
                        'Content': xml_dict.get('Content')
                    }
                }
            else:
                resp_dict = {
                    'xml': {
                        'ToUserName': xml_dict.get('FromUserName'),
                        'FromUserName': xml_dict.get('ToUserName'),
                        'CreateTime': int(time.time()),
                        'MsgType': 'text',
                        'Content': ''
                    }
                }
            resp_xml_str = xmltodict.unparse(resp_dict)
            return resp_xml_str


@app.route("/wechat8000/index")
def index():
    code = request.args.get('code')
    if not code:
        return u"确实code参数"
    url = "https://api.weixin.qq.com/sns/oauth2/access_token?appid=%s&secret=%s&code=%s&grant_type=authorization_code" % (WECHAT_APPID, WECHAT_APPSECRET, code)
    response = urllib2.urlopen(url)
    json_str = response.read()
    resp_dict = json.loads(json_str)
    if 'errcode' in resp_dict:
        return u'获取access_token失败'
    access_token = resp_dict.get('access_token')
    open_id = resp_dict.get('openid')
    url = 'https://api.weixin.qq.com/sns/userinfo?access_token=%s&openid=%s&lang=zh_CN' % (access_token, open_id)
    response = urllib2.urlopen(url)
    user_json_str = response.read()
    user_dict_data = json.loads(user_json_str)
    if 'errcode' in user_dict_data:
        return u'获取用户信息失败'
    else:
        return render_template("index.html", user=user_dict_data)


if __name__ == '__main__':
    app.run(port=8000, debug=True)