def test(num):
    print("在函数内部 %d 对应的内存地址是 %d" % (num, id(num)))
    pass

    result = "hello"
    print("函数要返回数据的内存地址是 %d" % id(result))
    return result


a = 10

print("a 变量保存数据的内存地址是 %d" % id(a))

r = test(a)
print("%s 的内存地址是 %d" % (r, id(r)))
