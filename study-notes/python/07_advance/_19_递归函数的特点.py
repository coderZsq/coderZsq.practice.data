def sum_number(num):
    print(num)
    if num == 1:
        return
    sum_number(num - 1)


sum_number(3)
