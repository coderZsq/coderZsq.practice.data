result = 0

i = 0

while i <= 100:
    if i % 2 == 0:
        print(i)
        result += i
    i += 1

print("0~100之间的偶数累加结果 = %d" % result)
