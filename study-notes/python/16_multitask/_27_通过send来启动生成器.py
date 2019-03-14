def create_num(all_num):
    a, b = 0, 1
    current_mum = 0
    while current_mum < all_num:
        ret = yield a
        print(">>>ret>>>", ret)
        a, b = b, a + b
        current_mum += 1


obj = create_num(10)
# obj.send(None)
ret = next(obj)
print(ret)

ret = obj.send("message")
print(ret)
