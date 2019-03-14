students = [
    {
        "name": "阿土"
    },
    {
        "name": "小美"
    }
]

find_name = "张三"

for stu_dict in students:
    print(stu_dict)
    if stu_dict["name"] == find_name:
        print("找到了 %s " % find_name)
        break
else:
    print("抱歉没有找到: %s" % find_name)

print("循环结束")
