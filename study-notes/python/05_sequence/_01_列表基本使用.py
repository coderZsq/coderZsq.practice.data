name_list = ["zhangsan", "lisi", "wangwu"]

print(name_list[0])

print(name_list.index("lisi"))

name_list[1] = "李四"

name_list.append("王小二")
name_list.insert(1, "小美眉")

temp_list = ["孙悟空", "猪二哥", "沙师弟"]
name_list.extend(temp_list)

name_list.remove("wangwu")
name_list.pop()
name_list.pop(3)
name_list.clear()

print(name_list)
