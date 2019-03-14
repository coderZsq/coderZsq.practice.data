import re


def index():
    with open("./templates/index.html", encoding="utf-8") as f:
        content = f.read()
    my_stock_info = ">>>>>>>>>>>>>>>"
    content = re.sub(r"\{%content%\}", my_stock_info, content)
    return content


def center():
    with open("./templates/center.html", encoding="utf-8") as f:
        return f.read()


URL_FUNC_DICT = {
    "/index.py": index,
    "/center.py": center
}


def application(env, start_response):
    start_response("200 ok", [('Content-Type', 'text/html;charset=utf-8')])
    file_name = env['PATH_INFO']
    # if file_name == "/index.py":
    #     return index()
    # elif file_name == "/center.py":
    #     return center()
    # return 'Hello World! 中文'

    func = URL_FUNC_DICT[file_name]
    return func()
