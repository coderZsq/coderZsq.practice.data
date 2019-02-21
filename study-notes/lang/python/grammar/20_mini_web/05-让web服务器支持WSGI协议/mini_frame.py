def application(environ, start_response):
    start_response("200 ok", [('Content-Type', 'text/html;charset=utf-8')])
    return 'Hello World! 中文'
