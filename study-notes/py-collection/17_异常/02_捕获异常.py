# 提示用户输入2个整数，最后打印2个整数的商
try:
    a = int(input('请输入第1个整数：'))
    print(1)

    b = int(input('请输入第2个整数：'))
    print(2)

    print(f'a除以b等于{a / b}')
    print(3)
except:
    print('出现了异常')
else:
    print('没有出现异常')
finally:
    print('执行完毕！')

print(4)
