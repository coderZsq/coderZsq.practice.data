def sum_numbers(*args):
# def sum_numbers(args):
    num = 0
    print(args)
    for n in args:
        num += n
    return num


# result = sum_numbers((1, 2, 3, 4, 5))
result = sum_numbers(1, 2, 3, 4, 5)

print(result)
