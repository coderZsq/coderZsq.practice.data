import re
import urllib.parse
from pymysql import connect


# URL_FUNC_DICT = {
#     "/index.py": index,
#     "/center.py": center
# }

URL_FUNC_DICT = dict()


def route(url):
    def set_func(func):
        URL_FUNC_DICT[url] = func

        def call_func(*args, **kwargs):
            return func(*args, **kwargs)
        return call_func
    return set_func


@route(r"/index.html")
def index(ret):
    with open("./templates/index.html", encoding="utf-8") as f:
        content = f.read()
    # infos = ">>>>>>>>>>>>>>>"
    # content = re.sub(r"\{%content%\}", infos, content)
    conn = connect(host="localhost", port=3306, user="root", password="root", database="movie", charset="utf8")
    cursor = conn.cursor()
    cursor.execute("select * from top250;")
    infos = cursor.fetchall()
    cursor.close()
    conn.close()
    tr_template = """
        </br>
        <tr>
            <td>%s</td>
            <td>%s</td>
            <td>%s</td>
            <td>%s</td>
        </tr>
    """
    html = ""
    for line_info in infos:
        html += tr_template % (line_info[0], line_info[1], line_info[2], line_info[3])
    content = re.sub(r"\{%content%\}", html, content)
    return content


@route(r"/center.html")
def center(ret):
    with open("./templates/center.html", encoding="utf-8") as f:
        return f.read()


@route(r"/add/(\d+)\.html")
def add_focus(ret):
    code = ret.group(1)
    return "add (%s) ok ...." % code


@route(r"/del/(\d+)\.html")
def del_focus(ret):
    code = ret.group(1)
    return "del (%s) ok ...." % code


@route(r"/update/(\d+)\.html")
def show_update_page(ret):
    code = ret.group(1)
    with open("./templates/update.html", encoding="utf-8") as f:
        return f.read()
    # return "update (%s) ok ...." % code


@route(r"/update/(\d+)/(.*)\.html")
def save_update_page(ret):
    code = ret.group(1)
    modify = ret.group(2)
    modify = urllib.parse.unquote(modify)
    return "update %s/%s" % (code, modify)


def application(env, start_response):
    start_response("200 ok", [('Content-Type', 'text/html;charset=utf-8')])
    file_name = env['PATH_INFO']
    # if file_name == "/index.py":
    #     return index()
    # elif file_name == "/center.py":
    #     return center()
    # return 'Hello World! 中文'

    try:
        # func = URL_FUNC_DICT[file_name]
        # return func()
        # return URL_FUNC_DICT[file_name]()
        for url, func in URL_FUNC_DICT.items():
            # {
            #   r"/index.html":index,
            #   r"/center.html":center,
            #   r"/add/\d+\.html":add_focus
            # }
            ret = re.match(url, file_name)
            if ret:
                return func(ret)
    except Exception as ret:
        return "产生了异常: %s" % str(ret)
