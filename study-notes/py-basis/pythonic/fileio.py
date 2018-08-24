
def rw():
    s = '你好'
    print(s.encode('utf8'))
    print(s.encode('gbk'))
    print(b'\xe4\xbd\xa0\xe5\xa5\xbd'.decode('gbk'))
    print(b'\xe4\xbd\xa0\xe5\xa5\xbd'.decode('utf8'))

    f = open('py2.txt', 'wb')
    s = '你好'
    f.write(s.encode('gbk'))
    f.close()
    f = open('py2.txt', 'rb')
    t = f.read()
    print(t.decode('gbk'))

    f = open('py3.txt', 'wt', encoding='utf8')
    f.write('你好')
    f.close()
    f = open('py3.txt', 'rt', encoding='utf8')
    t = f.read()
    print(t)


if __name__ == '__main__':
    rw()
    pass
