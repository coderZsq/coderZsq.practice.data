month = int(input('请输入月份：'))

if month < 1 or month > 12:
    print('非法输入')
elif month == 12 or 1 <= month <= 2:
    print('冬季')
elif month <= 5:  # 3 <= month <= 11
    print('春季')
elif month <= 8:  # 6 <= month <= 11
    print('夏季')
else:  # 9 <= month <= 11
    print('秋季')


# if 3 <= month <= 5:
#     print('春季')
# elif 6 <= month <= 8:
#     print('夏季')
# elif 9 <= month <= 11:
#     print('秋季')
# elif month == 12 or 1 <= month <= 2:
#     print('冬季')
# else:
#     print('非法输入')

# if month == 3 or month == 4 or month == 5:
#     print('春季')
# elif month == 6 or month == 7 or month == 8:
#     print('夏季')
# elif month == 9 or month == 10 or month == 11:
#     print('秋季')
# elif month == 12 or month == 1 or month == 2:
#     print('冬季')
# else:
#     print('非法输入')
