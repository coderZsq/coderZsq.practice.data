import requests
from collections import Iterable, Iterator
from itertools import islice

def iterator():
    def iterable():
        l = [1, 2, 3, 4]
        s = 'abcde'
        for x in l:
            print(x)
        for x in s:
            print(x)
        t = iter(l)
        print(t.__next__())
        print(t.__next__())
        print(t.__next__())
        print(t.__next__())
        # print(t.__next__())  # StopIteration
    iterable()

    class WeatherIterator(Iterator):
        def __init__(self, cities):
            self.cities = cities
            self.index = 0

        def getWeather(self, city):
            r = requests.get('http://wthrcdn.etouch.cn/weather_mini?city=' + city)
            data = r.json()['data']['forecast'][0]
            return '%s:, %s, %s ' % (city, data['low'], data['high'])

        def __next__(self):
            if self.index == len(self.cities):
                raise StopIteration
            city = self.cities[self.index]
            self.index += 1
            return self.getWeather(city)

    class WeatherIterable(Iterable):
        def __init__(self, cities):
            self.cities = cities;

        def __iter__(self):
            return WeatherIterator(self.cities)

    for x in WeatherIterable(['北京', '上海', '广州', '深圳']):
        print(x)


def generater():
    def f():
        print('in f(), 1')
        yield 1
        print('in f(), 2')
        yield 2
        print('in f(), 3')
        yield 3
    g = f()
    # print(g.__next__())
    # print(g.__next__())
    # print(g.__next__())
    # print(g.__next__())  # StopIteration
    for x in g:
        print(x)
    print(g.__iter__() is g)

    class PrimeNumbers:
        def __init__(self, start, end):
            self.start = start
            self.end = end

        def isPrimeNum(self, k):
            if k < 2:
                return False

            for i in range(2, k):
                if k % i == 0:
                    return False

            return True

        def __iter__(self):
            for k in range(self.start, self.end + 1):
                if self.isPrimeNum(k):
                    yield k

    for x in PrimeNumbers(1, 100):
        print(x)


def reversed_iterator():
    l = [1, 2, 3, 4, 5]
    l.reverse()
    print(l)
    l = [1, 2, 3, 4, 5]
    print(l[::-1])
    for x in reversed(l):
        print(x)

    class FloatRange:
        def __init__(self, start, end, step=0.1):
            self.start = start
            self.end = end
            self.step = step
        
        def __iter__(self):
            t = self.start
            while t <= self.end:
                yield t
                t += self.step

        def __reversed__(self):
            t = self.end
            while t >= self.start:
                yield t
                t -= self.step

    for x in FloatRange(1.0, 4.0, 0.5):
        print(x)

    for x in reversed(FloatRange(1.0, 4.0, 0.5)):
        print(x)

def iterator_sliced():
    f = open('./iterable.py')
    lines = f.readlines()
    print(lines[10:30])
    
    f.seek(0)
    for line in f:
        print(line)
        
    f.seek(0)
    for line in islice(f, 10, 30):
        print(line)

    l = range(20)
    print(l)
    t = iter(l)
    for x in islice(t, 5, 10):
        print(x)
    for x in t:
        print(x)


if __name__ == '__main__':
    # iterator()
    # generater()
    # reversed_iterator()
    iterator_sliced()
    pass
