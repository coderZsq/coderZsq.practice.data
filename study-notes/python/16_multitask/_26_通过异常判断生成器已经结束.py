def create_num(all_num):
    a, b = 0, 1
    current_mum = 0
    while current_mum < all_num:
        # print(a)
        yield a
        a, b = b, a + b
        current_mum += 1
    return "ok...."


obj2 = create_num(50)
while True:
    try:
        ret = next(obj2)
        print(ret)
    except Exception as ret:
        print(ret.value)
        break
