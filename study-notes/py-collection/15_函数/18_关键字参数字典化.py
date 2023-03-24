# 编写一个函数：可以打印个人信息（姓名、年龄、城市等，且这些信息都是可选的）
def show_info(**info):
    if 'name' in info:
        print('姓名 =', info['name'])

    if 'age' in info:
        print('年龄 =', info['age'])

    if 'city' in info:
        print('城市 =', info['city'])

    print(info)


show_info(name='MJ', age=18, city='广州', weight=188, height=190)
# show_info(age=18, city='广州')
# show_info(name='MJ', city='广州')
# show_info(city='广州')
# show_info(name='MJ', age=18)
# show_info(age=18)
# show_info(name='MJ')

# def show_info(name=None, age=None, city=None):
#     if name:
#         print(f'姓名 = {name}')
#     if age:
#         print(f'年龄 = {age}')
#     if city:
#         print(f'城市 = {city}')
#     print('-' * 30)

# def show_info(name=None, age=None, city=None):
#     name and print(f'姓名 = {name}')
#     age and print(f'年龄 = {age}')
#     city and print(f'城市 = {city}')
#     print('-' * 30)
