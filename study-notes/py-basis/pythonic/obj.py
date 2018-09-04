import sys
from telnetlib import Telnet
from sys import stdin, stdout
from collections import deque

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

if __name__ == '__main__':
    # t1()
    # t2()
    t3()
    pass

