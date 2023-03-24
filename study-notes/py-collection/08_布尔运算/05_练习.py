score = int(input('请输入分数：'))

if score < 0 or score > 100:
    print('非法输入')
elif score >= 90:  # [0, 100]
    # [90, 100]
    print('A')
elif score >= 80:  # [0, 89]
    # [80, 89]
    print('B')
elif score >= 70:  # [0, 79]
    # [70, 79]
    print('C')
elif score >= 60:  # [0, 69]
    # [60, 69]
    print('D')
else:  # [0, 59]
    print('E')


if 90 <= score <= 100:
    print('A')
elif 80 <= score <= 89:
    print('B')
elif 70 <= score <= 79:
    print('C')
elif 60 <= score <= 69:
    print('D')
elif 0 <= score <= 59:
    print('E')
else:
    print('非法输入')
