def test(a: int | list, b: str) -> tuple | int:
    print(a)
    print(b)
    return 40


# d = test(50, 'kkk')
d = test(60, 'kkk')
print(d[0])
print(d[1])


age: int | None = 20

age += 10

age = None

# age = '76576'
# age += '53454'
# age = [11, 22, 33]

