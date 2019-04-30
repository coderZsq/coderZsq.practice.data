# coding:utf-8

from . import api
from flask_.utils.captcha.captcha import captcha
from flask_ import redis_store
from flask_ import constants
from flask import current_app, jsonify, make_response
from flask_.utils.response_code import RET


@api.route("/image_codes/<image_code_id>")
def get_image_code(image_code_id):
    name, text, image_data = captcha.generate_captcha()
    # redis_store.set("image_code_%s" % image_code_id, text)
    # redis_store.expire("image_code_%s" % image_code_id, constants.IMAGE_CODE_REDIS_EXPIRES)
    try:
        redis_store.setex("image_code_%s" % image_code_id, constants.IMAGE_CODE_REDIS_EXPIRES, text)
    except Exception as e:
        current_app.logger.error(e)
        return jsonify(error=RET.DBERR, errmsg="save image code id failed")
    resp = make_response(image_data)
    resp.headers["Content-Type"] = "image/jpg"
    return resp