# def run(name, breed, age):
#     """
#     让一只狗跑步
#     :param name: 名字
#     :param breed: 品种
#     :param age: 年龄
#     """
#     print(f'一只名字叫{name}的{age}岁{breed}跑起来了！')
#
#
# run('宝哥', '柴犬', 5)
# run('旺财', '中华田园犬', 3)
# run('拆哥', '哈士奇', 4)

def run(dog: dict):
    """
    让一只狗跑步
    :param dog: 狗
    """
    print(f'一只名字叫{dog["name"]}的{dog["age"]}岁{dog["breed"]}跑起来了！')


run({
    'name': '宝哥',
    'breed': '柴犬',
    'age': 5
})
run({
    'name': '旺财',
    'breed': '中华田园犬',
    'age': 3
})
run({
    'name': '拆哥',
    'breed': '哈士奇',
    'age': 4
})

run({
    'title': '7777',
    'weight': 199
})
