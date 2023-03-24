s = [56, 78, 100, 89, 0, 96]

# 方法4
if all(s):  # 所有分数都不为0
    print('没有0分的学员')
else:
    print('有0分的学员')

# 方法3
# # 检查
# # 是否有0分的学员
# zero = False
# for i in s:
#     if i:
#         continue
#     zero = True
#     break
#
# # 打印
# if zero:
#     print('有0分的学员')
# else:
#     print('没有0分的学员')

# 方法2
# # 检查
# # 是否有0分的学员
# zero = False
# for i in s:
#     if not i:
#         zero = True
#         break
#
# # 打印
# if zero:
#     print('有0分的学员')
# else:
#     print('没有0分的学员')


# 方法1
# # 检查
# # 是否有0分的学员
# zero = False
# for i in s:
#     if i == 0:
#         zero = True
#         break
#
# # 打印
# if zero:
#     print('有0分的学员')
# else:
#     print('没有0分的学员')
