a = 999

if not (a == 5 or 10 < a <= 15 or 20 < a <= 25):
    print(1)
else:
    print(0)

if not ((a < 10 and a != 5) or 15 < a <= 20 or a > 25):
    print(0)
else:
    print(1)

if not (a < 5 or 5 < a <= 10 or 15 < a <= 20 or a > 25):
    print(0)
else:
    print(1)

# if a == 5 or 10 < a <= 15 or 20 < a <= 25:
#     print(0)
# else:
#     print(1)

# if (a < 10 and a != 5) or 15 < a <= 20 or a > 25:
#     print(1)
# else:
#     print(0)

# if a < 5 or 5 < a <= 10 or 15 < a <= 20 or a > 25:
#     print(1)
# else:
#     print(0)
