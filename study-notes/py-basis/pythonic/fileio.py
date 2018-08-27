import struct
import array
import mmap
import os
import stat
import time
from tempfile import TemporaryFile, NamedTemporaryFile

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

def rwb():
    f = open('龙卷风.wav', 'rb')
    info = f.read(44)
    print(info)
    print(struct.unpack('h', info[22:24]))
    print(struct.unpack('i', info[24:28]))
    print(struct.unpack('h', info[34:36]))
    f.seek(0, 2)
    print(f.tell())

    n = int((f.tell() - 44) / 2)
    buf = array.array('h', (0 for _ in range(n)))
    f.seek(44)
    print(f.readinto(buf))
    print(buf[0])
    print(buf[5])
    print(buf[10])

    for i in range(n):
        buf[i] = int(buf[i] / 8)

    f2 = open('tornado.wav', 'wb')
    f2.write(info)
    buf.tofile(f2)
    f2.close()

def buf():
    f = open('demo.txt', 'wt',  encoding='utf8')
    f.write('abc')
    f.write('+' * 4093)
    f.write('-')
    f.write('*' * 4095)
    f.write('x')

    f = open('demo2.txt', 'wt', buffering=2048, encoding='utf8')
    f.write('+' * 1024)
    f.write('+' * 1023)
    f.write('-')

    f = open('demo3.txt', 'wt', buffering=1, encoding='utf8')
    f.write('abcd')
    f.write('1234')
    f.write('\n')
    f.write('xyz\n')

    f = open('demo4.txt', 'wt', buffering=1, encoding='utf8')
    f.write('a')
    f.write('b')
    f.write('xyz')

def mm():
    f = open('demo.bin', 'rb')
    print(f.fileno())
    m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_WRITE)
    print(m[0])
    print(m[10:20])
    m[0] = '\x88'
    m[4:8] = '\xff' * 4
    m = mmap.mmap(f.fileno(), mmap.PAGESIZE * 8, access=mmap.ACCESS_WRITE, offset=mmap.PAGESIZE * 4)
    m[:0x1000] = '\xaa' * 0x1000

def fs():
    print(os.stat('fileio.py'))
    s = os.stat('fileio.py')
    print(s.st_mode)
    print(bin(s.st_mode))
    print(stat.S_ISDIR(s.st_mode))
    print(stat.S_ISREG(s.st_mode))
    print(s.st_mode & stat.S_IRUSR)
    print(s.st_mode & stat.S_IXUSR)
    print(s.st_atime)
    print(time.localtime(s.st_atime))
    print(s.st_size)

    print(os.path.isdir('fileio.py'))
    print(os.path.islink('fileio.py'))
    print(os.path.isfile('fileio.py'))
    print(os.path.getatime('fileio.py'))
    print(os.path.getsize('fileio.py'))

def tmp():
    f = TemporaryFile()
    f.write('abcdefg' * 100000)
    f.seek(0)
    f.read(100)

    ntf = NamedTemporaryFile()
    print(ntf.name)

if __name__ == '__main__':
    # rw()
    # rwb()
    # buf()
    # mm()
    # fs()
    # tmp()
    pass

