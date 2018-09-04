import sys
from telnetlib import Telnet
from sys import stdin, stdout
from collections import deque
from math import pi
from functools import total_ordering
from abc import ABCMeta, abstractmethod
import gc
import weakref
from operator import methodcaller

def t1():
    class IntTuple(tuple):

        def __new__(cls, iterable):
            g = (x for x in iterable if isinstance(x, int) and x > 0)
            return super().__new__(cls, g)

        def __init__(self, iterable):
            #before
            super().__init__(iterable)
            #after
    t = IntTuple(tuple([1, -1, 'abc', 6, ['x', 'y'], 3]))
    print(t)

def t2():
    class Player(object):
        def __init__(self, uid, name, status=0, level=1):
            self.uid = uid
            self.name = name
            self.stat = status
            self.level = level

    class Player2(object):
        __slots__ = ['uid', 'name', 'stat', 'level']
        def __init__(self, uid, name, status=0, level=1):
            self.uid = uid
            self.name = name
            self.stat = status
            self.level = level

    p1 = Player('0001', 'Jim')
    p2 = Player2('0001', 'Jim')
    print(dir(p1))
    print(dir(p2))
    print(set(dir(p1)) - set(dir(p2)))
    print(p1.__dict__)
    p1.x = 123
    print(p1.__dict__)
    p1.__dict__['y'] = 99
    print(p1.__dict__)
    del p1.__dict__['x']
    print(p1.__dict__)

    print(sys.getsizeof(p1.__dict__))

def t3():
    with open('demo.txt', 'w') as f:
        f.write('abcdef')
        f.writelines(['xyz\n', '123\n'])
        # f.close()

    class TelnetClient(object):
        def __init__(self, addr, port=23):
            self.addr = addr
            self.port = port
            self.tn = None
        
        def start(self):
            raise Exception('Test')
            #user
            t = self.tn.read_until('login: ')
            stdout.write(t)
            user = stdin.readline()
            self.tn.write(user)

            #password
            t = self.tn.read_until('Password: ')
            if t.startswith(user[:-1]): t = t[len(user) + 1]
            stdout.write(t)
            self.tn.write(stdin.readline(0))

            t = self.tn.read_until('$ ')
            stdout.write(t)
            while True:
                uinput = stdin.readline()
                if not uinput:
                    break
                self.history.append(uinput)
                self.tn.write(uinput)
                t = self.tn.read_until('$ ')
                stdout.write(t[len(uinput) + 1:])

        def cleanup(self):
            pass

        def __enter__(self):
            self.tn = Telnet(self.addr, self.port)
            self.history = deque()
            return self

        def __exit__(self, exe_type, exc_val, exc_tb):
            print 'In __exit__'
            self.tn.close()
            self.tn = None
            with open(self.addr + '_history.txt', 'w') as f:
                f.writelines(self.history)

    with TelnetClient('127.0.0.1') as client:
        client.start()
    print 'END'
    '''
    client = TelnetClient('127.0.0.1')
    print '\nstart...'
    client.start()
    print '\ncleanup'
    client.cleanup()
    '''

def t4():
    class Circle(object):
        def __init__(self, radius):
            self.radius = radius

        def getRadius(self):
            return round(self.radius, 2)

        def setRadius(self, value):
            if not isinstance(value, (int, long, float)):
                raise ValueError('wrong type.')
            self.radius = float(value)

        def getArea(self):
            return self.radius ** 2 * pi

        R = property(getRadius, setRadius)

    c = Circle(3.2)
    print c.R
    c.R = 5.9
    print c.R

def t5():
    @total_ordering
    class Shape(object):
        @abstractmethod
        def area(self):
            pass

        def __lt__(self, obj):
            print 'in __lt__'
            if not isinstance(obj, Shape):
                raise TypeError('obj is not Shape')
            return self.area() < obj.area()

        def __eq__(self, obj):
            print 'in __le__'
            if not isinstance(obj, Shape):
                raise TypeError('obj is not Shape')
            return self.area() == obj.area()

    class Rectangle(Shape):
        def __init__(self, w, h):
            self.w = w
            self.h = h

        def area(self):
            return self.w * self.h


    class Circle(Shape):
        def __init__(self, r):
            self.r = r
        
        def area(self):
            return self.r ** 2 * 3.14

    r1 = Rectangle(5, 3)
    r2 = Rectangle(4, 4)
    c1 = Circle(3)
    print c1 <= r1
    print r1 > c1

def t6():
    class Attr(object):
        def __init__(self, name, type_):
            self.name = name
            self.type_ = type_

        def __get__(self, instance, cls):
            return instance.__dict__[self.name]

        def __set__(self, instance, value):
            if not isinstance(value, self.type_):
                raise TypeError('expected an %s' % self.type_)
            instance.__dict__[self.name] = value

        def __delete__(self, instance):
            del instance.__dict__[self.name]

    class Person(object):
        name = Attr('name', str)
        age = Attr('age', int)
        height = Attr('height', float)

    p = Person()
    p.name = 'Castie!'
    print p.name

def t7():
    class A(object):
        def __del__(self):
            print 'in A.__del__'

    a = A()
    print sys.getrefcount(a) - 1
    a2 = a
    print sys.getrefcount(a) - 1
    del a2
    print sys.getrefcount(a) - 1
    # a = 5

    a_wref = weakref.ref(a)
    a2 = a_wref()
    print a is a2
    del a
    del a2
    print a_wref() is None

    class Data(object):
        def __init__(self, value, owner):
            self.owner = weakref.ref(owner)
            self.value = value

        def __str__(self):
            return "%s's data, value is %s" % (self.owner, self.value)

        def __del__(self):
            print 'in Data.__del__'

    class Node(object):
        def __init__(self, value):
            self.data = Data(value, self)
        
        def __del__(self):
            print 'in Node.__del__'

    node = Node(100)
    del node
    gc.collect()
    raw_input('wait...')

def t8():
    class Circle(object):
        def __init__(self, r):
            self.r = r

        def area(self):
            return self.r ** 2 * 3.14

    class Triangle(object):
        def __init__(self, a, b, c):
            self.a = a
            self.b = b
            self.c = c

        def getArea(self):
            a, b, c = self.a, self.b, self.c
            p = (a + b + c) / 2
            area = (p * (p - a) * (p - b) * (p - c)) ** 0.5
            return area

    class Rectangle(object):
        def __init__(self, w, h):
            self.w = w
            self.h = h
    
        def get_area(self):
            return self.w * self.h

    def getArea(shape):
        for name in ('area', 'getArea', 'get_area'):
            f = getattr(shape, name, None)
            if f:
                return f()
        pass

    shape1 = Circle(2)
    shape2 = Triangle(3, 4, 5)
    shape3 = Rectangle(6, 4)
    shapes = [shape1, shape2, shape3]
    print map(getArea, shapes)

    s = 'abc123abc456'
    print s.find('abc', 4)
    print methodcaller('find', 'abc', 4)(s)


if __name__ == '__main__':
    # t1()
    # t2()
    # t3()
    # t4()
    # t5()
    # t6()
    # t7()
    t8()
    pass

