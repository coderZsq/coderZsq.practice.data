poem_str = "登黄鹤楼\t 王之涣 \t 白日依山尽\t\n 黄河入海流 \t\t 欲穷千里目 \t\n 更上一层楼"

print(poem_str)

poem_list = poem_str.split()
print(poem_list)

result = " ".join(poem_list)
print(result)
