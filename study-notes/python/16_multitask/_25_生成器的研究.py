def create_num(all_num):
    print("----1----")
    a, b = 0, 1
    current_mum = 0
    while current_mum < all_num:
        print("----2----")
        # print(a)
        yield a
        print("----3----")
        a, b = b, a + b
        current_mum += 1
        print("----4----")


obj = create_num(10)
obj2 = create_num(2)
ret = next(obj)
print("obj:", ret)
ret = next(obj)
print("obj:", ret)
ret = next(obj2)
print("obj2:", ret)
ret = next(obj)
print("obj:", ret)
ret = next(obj)
print("obj:", ret)
ret = next(obj)
print("obj:", ret)
ret = next(obj2)
print("obj2:", ret)
ret = next(obj2)
print("obj2:", ret)
# for num in obj:
#     print(num)
