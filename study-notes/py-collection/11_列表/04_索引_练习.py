day = int(input('请输入整数：'))

# 方法3
# 0用来占位
days = [0, '一', '二', '三', '四', '五', '六', '天']

if 1 <= day <= 7:
    print(f'星期{days[day]}')
else:
    print('非法输入')

# 方法2
# days = ['一', '二', '三', '四', '五', '六', '天']
#
# if 1 <= day <= 7:
#     print(f'星期{days[day - 1]}')
# else:
#     print('非法输入')

# 方法1
# days = [
#     '星期一', '星期二', '星期三',
#     '星期四', '星期五', '星期六', '星期天'
# ]
# if 1 <= day <= 7:
#     print(days[day - 1])
# else:
#     print('非法输入')
