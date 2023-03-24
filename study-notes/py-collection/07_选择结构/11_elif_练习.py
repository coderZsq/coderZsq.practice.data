a = 111
b = 22
c = 22

if a > b:
    if b > c:  # a > b > c
        print(f'中间值是{b}')
    elif a > c:  # a > b且c >= b且 a > c => a > c >= b
        print(f'中间值是{c}')
    else:
        print(f'中间值是{a}')
else:  # b >= a
    if c > b:  # c > b >= a
        print(f'中间值是{b}')
    elif a > c:  # b >= a > c
        print(f'中间值是{a}')
    else:
        print(f'中间值是{c}')
