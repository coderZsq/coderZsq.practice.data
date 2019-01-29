from functools import update_wrapper, wraps, WRAPPER_ASSIGNMENTS, WRAPPER_UPDATES
# from inspect import signature
import time
import logging
from random import randint

def t1():
    def memo(func):
        cache = {}
        def wrap(*args):
            if args not in cache:
                cache[args] = func(*args)
            return cache[args]
        return wrap
    @memo  
    def fibonacci(n):
        if n <= 1:
            return 1
        return fibonacci(n - 1) + fibonacci(n - 2)

    print fibonacci(50)
    @memo
    def climb(n, steps):
        count = 0
        if n == 0:
            count = 1
        elif n > 0:
            for step in steps:
                count += climb(n - step, steps)
        return count
    print climb(10, (1, 2, 3))

def t2():
    def mydecorator(func):
        @wraps(func)
        def wrapper(*args, **kargs):
            '''wrapper function'''
            print 'In wrapper'
            func(*args, **kargs)
        # wrapper.__name__ = func.__name__
        # update_wrapper(wrapper, func)
        return wrapper

    @mydecorator
    def example():
        '''example function'''
        print('In example')

    print example.__name__
    print example.__doc__
    # print WRAPPER_ASSIGNMENTS
    # print WRAPPER_UPDATES

def t3():
    def typeassert(*ty_args, **ty_kargs):
        def decorator(func):
            sig = signature(func)
            btypes = sig.bind_partial(*ty_args, **ty_kargs).arguments
            def wrapper(*args, **kargs):
                for name, obj in sig.bind(*args, **kargs).arguments.items():
                    if name in btypes:
                        if not isinstance(obj, btypes[name]):
                            raise TypeError('"%s" must be "%s"' % (name, btypes[name]))
                return func(*args, **kargs)
            return wrapper
        return decorator

    @typeassert(int, str, list)
    def f(a, b, c):
        print(a, b, c)

    f(1, 'abc', [1, 2, 3])
    f(1, 2, [1, 2, 3])


def t4():
    def warn(timeout):
        timeout = [timeout]
        def decorator(func):
            def wrapper(*args, **kargs):
                start = time.time()
                res = func(*args, **kargs)
                used = time.time() - start
                if used > timeout[0]:
                    msg = '"%s" : %s > %s' % (func.__name__, used, timeout[0])
                    logging.warn(msg)
                return res
            return wrapper
            def setTimeout(k):
                # nonlocal timeout
                # timeout = k
                timeout[0] = k
            wrapper.setTimeout = setTimeout
        return decorator

    @warn(1.5)
    def test():
        print('In test')
        while randint(0, 1):
            time.sleep(0.5)

    for _ in range(30):
        test()

if __name__ == '__main__':
    # t1()
    # t2()
    # t3()
    t4()
    pass
