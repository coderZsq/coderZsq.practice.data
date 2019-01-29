from random import randint, sample
from collections import namedtuple
from collections import Counter
from collections import OrderedDict
from collections import deque
from functools import reduce
from time import time
import re

def list_filter():
    data = [randint(-10, 10) for _ in range(10)]
    print(data)
    print(list(filter(lambda x: x >= 0, data)))
    print([x for x in data if x >= 0])

def dict_filter():
    data = {x: randint(60, 100) for x in range(1, 21)}
    print(data)
    print({k: v for k, v in data.items() if v > 90})

def set_filter():
    data = set([randint(-10, 10) for _ in range(10)])
    print(data)
    print({x for x in data if x % 3 == 0})


def filtered():
    list_filter()
    dict_filter()
    set_filter()

def tuplenamed():
    NAME, AGE, SEX, EMAIL = range(4)
    profile = ('Castie!', 26, 'male', 'a13701777868@gmail.com')
    print(profile[NAME])
    if profile[AGE] >= 18: pass
    if profile[SEX] == 'male': pass

    Profile = namedtuple('Profile', ['name', 'age', 'sex', 'email'])
    p = Profile('Castie!', 26, 'male', 'a13701777868@gmail.com')
    print(p)
    p2 = Profile(name='Castie!', age=16, sex='male',email='a13701777868@gmail.com')
    print(p2)
    print(p.name)
    print(p.age)
    print(p.sex)


def frequency():
    data = [randint(0, 20) for _ in range(30)]
    print(data)
    c = dict.fromkeys(data, 0)
    print(c)
    for x in data:
        c[x] += 1
    print(c)

    c2 =  Counter(data)
    print(c2)
    print(c2.most_common(3))

    txt = open('pythonic.py').read()
    print(txt)
    c3 = Counter(re.split('\W+', txt))
    print(c3)
    print(c3.most_common(10))

def sort():
    print(sorted([9, 1, 2, 8, 5]))  
    data = {x: randint(60, 100) for x in 'xyzabc'}  
    print(data)
    print(sorted(data))
    print(data.keys())
    print(data.values())
    print(sorted(zip(data.values(), data.keys())))

    print(sorted(data.items(), key=lambda x: x[1]))

def commonkey():
    print(sample('abcdefg', 3))
    print(sample('abcdefg', randint(3, 6)))

    s1 = {x: randint(1, 4) for x in sample('abcdefg', randint(3, 6))}
    s2 = {x: randint(1, 4) for x in sample('abcdefg', randint(3, 6))}
    s3 = {x: randint(1, 4) for x in sample('abcdefg', randint(3, 6))}

    print(s1)
    print(s2)
    print(s3)

    res = []
    for k in s1:
        if k in s2 and k in s3:
            res.append(k)
    print(res)

    print(s1.keys() & s2.keys() & s3.keys())

    print(reduce(lambda a, b: a & b, map(dict.keys, [s1, s2, s3])))

def ordered_dict():
    data = {}
    data['Jim'] = (1, 35)
    data['Leo'] = (2, 37)
    data['Bob'] = (3, 40)
    for k in data: print(k)

    data = OrderedDict()
    data['Jim'] = (1, 35)
    data['Leo'] = (2, 37)
    data['Bob'] = (3, 40)
    for k in data: print(k)

    players = list('ABCDEFGH')
    start = time()
    for i in range(8):
        input()
        p = players.pop(randint(0, 7 - i))
        end = time()
        print(i + 1, p, end - start)
        data[p] = (i + 1, end - start)
        
    print
    print('-' * 20)
    for k in data:
        print(k, data[k])

def history_record():
    N = randint(0, 100)
    history = deque([], 5)    
    def guess(k):
        if k == N:
            print('right')
            return True
        if k < N:
            print('%s is less-than N' % k)
        else:
            print('%s is greater-than N' % k)
        return False
    while True:
        line = input('please input a number: ')
        if line.isdigit():
            k = int(line)
            history.append(k)
            if guess(k):
                break
        elif line == 'history' or line == 'h?':
            print (list(history))

if __name__ == '__main__':
    # filtered()
    # tuplenamed()
    # frequency()
    # sort()
    # commonkey()
    # ordered_dict()
    history_record()
    pass
