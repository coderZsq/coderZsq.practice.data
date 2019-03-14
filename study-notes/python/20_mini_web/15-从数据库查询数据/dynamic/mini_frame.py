import re
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


@route("/index.html")
def index():
    with open("./templates/index.html", encoding="utf-8") as f:
        content = f.read()
    # data = ">>>>>>>>>>>>>>>"
    # content = re.sub(r"\{%content%\}", data, content)
    conn = connect(host="localhost", port=3306, user="root", password="root", database="movie", charset="utf8")
    cursor = conn.cursor()
    cursor.execute("select * from top250;")
    data = cursor.fetchall()
    cursor.close()
    conn.close()
    content = re.sub(r"\{%content%\}", str(data), content)
    return content


@route("/center.html")
def center():
    with open("./templates/center.html", encoding="utf-8") as f:
        return f.read()


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
        return URL_FUNC_DICT[file_name]()
    except Exception as ret:
        return "产生了异常: %s" % str(ret)
