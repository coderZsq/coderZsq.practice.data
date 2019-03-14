import threading
import time


def test1():
    for i in range(5):
        print("-----test1---%d---" % i)
        time.sleep(1)


def main():
    print(threading.enumerate())
    t1 = threading.Thread(target=test1)
    print(threading.enumerate())
    t1.start()
    print(threading.enumerate())


if __name__ == '__main__':
    main()