# 计算1 + 3 + 5 + ... + n
def odd_sum(n):
    return sum(
        [i for i in range(1, n + 1, 2)]
    )

    # data = [i for i in range(1, n + 1, 2)]
    # return sum(data)

# def odd_sum(n):
#     ret = 0
#     for i in range(1, n + 1, 2):
#         ret += i
#     return ret


# 1 + 3 + 5 = 9
a = odd_sum(5)

# 1 + 3 + 5 = 9
b = odd_sum(6)

# 1 + 3 + 5 + 7 + 9 = 25
c = odd_sum(10)

print(a, b, c)

print(odd_sum(100))
