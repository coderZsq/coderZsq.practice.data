def demo(num, num_list):
    print("函数开始")
    num += num
    num_list += num_list
    # num_list.extend(num_list)
    print(num)
    print(num_list)
    print("函数完成")


gl_num = 9
gl_list = [1, 2, 3]
demo(gl_num, gl_list)
print(gl_num)
print(gl_list)
