def hello(name, times):
    for _ in range(times):
        print(f'Hi, {name}!')


d = {
    'name': 'Jake',
    'times': 3,
    'title': 'yyyy'
}
hello(**d)
hello(name='Jake', times=3, title='yyyy')

# hello(name='Jake', times=3)
# hello(name=d['name'], times=d['times'])

# hello('MJ', 5)
