# coding:utf-8

from werkzeug.routing import BaseConverter


class ReConverter(BaseConverter):
    def __init__(self, url_map, regex):
        super(ReConverter, self).__init__(url_map)
        self.regex = regex
