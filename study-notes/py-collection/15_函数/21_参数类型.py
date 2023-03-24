def hello(name: str, times: int):
    for _ in range(times):
        print(f'Hi, {name}!')


hello('MJ', 2)
# hello(2, 'MJ')


def test(a: list):
    a.append()
    a.extend()
