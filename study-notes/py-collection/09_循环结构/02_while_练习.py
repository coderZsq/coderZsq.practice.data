i = 1

# while i <= 10:
#     t = '奇' if i % 2 else '偶'
#     print('%02d - %s数' % (i, t))
#     i += 1

while i <= 10:
    t = '偶数'
    if i % 2:
        t = '奇数'
    print('%02d - %s' % (i, t))
    i += 1

# while i <= 10:
#     t = '奇数'
#     if i % 2 == 0:
#         t = '偶数'
#     print('%02d - %s' % (i, t))
#     i += 1