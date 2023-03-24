a = 1111
b = 3333
c = 2222

# if a > b:  # a > b
#     if a > c:  # a > b且a > c
#         print(f'最大值是{a}')
#     else:  # c >= a > b
#         print(f'最大值是{c}')
# else:  # b >= a
#     if b > c:  # b >= a且 b > c
#         print(f'最大值是{b}')
#     else:  # c >= b >= a
#         print(f'最大值是{c}')

# if a > b:
#     print(f'最大值是{a if a > c else c}')
# else:
#     print(f'最大值是{b if b > c else c}')

# if a > b:
#     print(f'最大值是{max(a, c)}')
# else:
#     print(f'最大值是{max(b, c)}')

print(max(a, b, c))
