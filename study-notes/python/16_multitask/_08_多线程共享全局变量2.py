import threading
import time


def test1(temp):
    temp.append(33)
    print("-----in test1 g_nums=%s-----" % str(temp))


def test2(temp):
    print("-----in test1 g_nums=%s-----" % str(temp))


g_nums = [11, 22]


def main():
    t1 = threading.Thread(target=test1, args=(g_nums,))
    t2 = threading.Thread(target=test2, args=(g_nums,))
    t1.start()
    time.sleep(1)
    t2.start()
    time.sleep(1)
    print("-----in main Thread g_nums = %s-----" % str(g_nums))


if __name__ == '__main__':
    main()
