## 接口文档

1. 接口名字
2. 描述 (描述清楚接口的功能)
3. url
4. 传入参数 
5. 传入参数
6. 返回值

接口: 获取图片验证码
描述: 前端访问, 可以获取到验证码图片

url: /api/v1.0/image_codes/<image_code_id>

传入参数:
格式: 路径参数 (参数是查询字符串, 请求体的表单, json, xml)

名字           类型      是否必须      说明
image_code_id 字符串       是    验证码图片的编号

返回值:
格式:  正常:图片   异常:json
名字      类型      是否必传    说明
errno    字符串       否      错误代码
errmsg   字符串       否      错误内容

实例:
'{"errno": "4001", "errmsg": "保存图片验证码失败"}'