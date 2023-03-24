# try:
#     a = int(input('请输入第1个整数：'))  # ValueError
#
#     b = int(input('请输入第2个整数：'))  # ValueError
#
#     print(f'a除以b等于{a / b}')  # ZeroDivisionError
#
#     s = [10, 20]
#     print(s[5])
# except ValueError:
#     print('输入的数据无法转成整数')
# except ZeroDivisionError:
#     print('0不能作为除数')
# except:
#     print('出现了其他的异常')

# try:
#     a = int(input('请输入第1个整数：'))
#
#     b = int(input('请输入第2个整数：'))
#
#     print(f'a除以b等于{a / b}')
# except (ValueError, ZeroDivisionError):
#     print('【输入的数据无法转成整数】或者【0不能作为除数】')

# try:
#     a = int(input('请输入第1个整数：'))
#
#     b = int(input('请输入第2个整数：'))
#
#     print(f'a除以b等于{a / b}')
# except ValueError as e:
#     print('输入的数据无法转成整数', e.args[0])
# except ZeroDivisionError as e:
#     print('0不能作为除数', e.args[0])
#
# try:
#     a = int(input('请输入第1个整数：'))
#
#     b = int(input('请输入第2个整数：'))
#
#     print(f'a除以b等于{a / b}')
# except (ValueError, ZeroDivisionError) as e:
#     print('【输入的数据无法转成整数】或者【0不能作为除数】', e.args[0])


try:
    a = int(input('请输入第1个整数：'))

    b = int(input('请输入第2个整数：'))

    print(f'a除以b等于{a / b}')
except BaseException as e:
    print('出现了异常', e.args[0])
