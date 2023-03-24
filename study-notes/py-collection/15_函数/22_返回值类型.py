# 计算所有奇数、偶数的和
def odd_even_sum(n: int) -> tuple:
    n += 1
    o = [i for i in range(1, n, 2)]
    e = [i for i in range(2, n, 2)]
    return sum(o), sum(e)


d = odd_even_sum(10)
print(d)

# Python的类型限制是很弱的
age: int = 10
age += 2
age = 'ppp'
print(age)

# age -= 1
# age = [11, 22]
