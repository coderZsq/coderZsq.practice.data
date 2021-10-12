# 记录生肖, 根据年份来判断生肖

chinese_zodiac = '猴鸡狗猪鼠牛虎兔龙蛇马羊'

year = int(input('请用户输入出身年份'))

if (chinese_zodiac[year % 12]) == '狗':
    print('狗年运势...')
