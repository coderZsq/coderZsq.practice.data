def index():
    with open("./templates/index.html") as f:
        content = f.read()
    return content


def center():
    with open("./templates/center.html") as f:
        return f.read()


def application(env, start_response):
    start_response("200 ok", [('Content-Type', 'text/html;charset=utf-8')])
    file_name = env['PATH_INFO']
    if file_name == "/index.py":
        return index()
    elif file_name == "/center.py":
        return center()
    return 'Hello World! 中文'
