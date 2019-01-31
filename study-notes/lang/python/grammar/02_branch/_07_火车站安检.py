has_ticket = True

knife_length = 20

if has_ticket:
    print("车票检查通过, 准备开始安检")
    if knife_length > 20:
        print("您携带的刀太长了, 有%s公分长!" % knife_length)
        print("不允许上车")
    else:
        print("安检已经通过, 祝您旅途愉快!")

else:
    print("大哥, 请先买票")
