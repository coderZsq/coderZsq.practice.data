import re
import os
import stat

def split():
    s = 'ab;cd|efg|hi,jkl|mn\topq;rst,uvw\txyz'
    print(s.split(';'))
    res = s.split(';')
    print(list(map(lambda x: x.split('|'), res)))
    t = []
    print(list(map(lambda x: t.extend(x.split('|')), res)))
    print(t)
    res = t
    t = []
    print(list(map(lambda x: t.extend(x.split(',')), res)))
    print(t)

    def mySplit(s, ds):
        res = [s]
        for d in ds:
            t = []
            list(map(lambda x: t.extend(x.split(d)), res))
            res = t
        return [x for x in res if x]

    print(mySplit(s, ';,|\t'))
    print(re.split('[,;\t|]+', s))


def endswith():
    print(os.listdir('.'))
    s = 'g.sh'
    print(s.endswith('.sh'))
    print(s.endswith('.py'))
    print(s.endswith(('.sh', '.py')))
    print([name for name in os.listdir('.') if name.endswith(('.lock', '.py'))])
    print(os.stat('string.py'))
    print(os.stat('string.py').st_mode)
    print(oct(os.stat('string.py').st_mode))
    os.chmod('string.py', os.stat('string.py').st_mode | stat.S_IXUSR)


def replace():
    log = '2016-05-23 10:59:27 status installed libc-bin'
    print(re.sub('(\d{4})-(\d{2})-(\d{2})', r'\2/\3/\1', log))
    print(re.sub('(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})',
                 r'\g<month>/\g<day>/\g<year>', log))


def concat():
    s1 = 'abcdefg'
    s2 = '12345'
    print(s1 + s2)
    print(str.__add__(s1, s2))
    print(s1 > s2)
    print(str.__gt__(s1, s2))

    pl = ['<0112>', '<32>', '<1024x768>', '<60>', '<1>', '<100.0>', '<500.0>']
    s = ''
    for p in pl:
        s += p
        print(s)
    print(s)

    print(';'.join(['abc', '123', 'xyz']))
    print(''.join(['abc', '123', 'xyz']))
    print(''.join(pl))

    l = ['abc', 123, 45, 'xyz']
    print(''.join([str(x) for x in l]))
    print(''.join(str(x) for x in l))


def align():
    s = 'abc'
    print(s.ljust(20))
    print(s.ljust(20, '='))
    print(s.rjust(20))
    print(len(s.rjust(20)))
    print(s.center(20))

    print(format(s, '<20'))
    print(format(s, '>20'))
    print(format(s, '^20'))

    d = {
        'DistCull': 500.0,
        'SmallCull': 0.04,
        'farclip': 477,
        'lodDist': 100.0,
        'trilinear': 40
    }
    print(d)
    print(d.keys())
    print(list(map(len, d.keys())))
    print(max(map(len, d.keys())))
    w = max(map(len, d.keys()))
    for k in d:
        print(k.ljust(w), ':', d[k])


def trim():
    s = '   abc     123    '
    print(s.strip())
    print(s.lstrip())
    print(s.rstrip())
    s = '---abc+++'
    print(s.strip('-+'))

    s = 'abc:123'
    print(s[:3] + s[4:])

    s = '\tabc\t123\txyz'
    print(s.replace('\t', ''))

    s = '\tabc\t123\txyz\ropq\r'
    print(re.sub('[\t\r]', '', s))
    
    s = 'abc1230323xyz'
    print(str.maketrans('abcxyz', 'xyzabc'))
    print(s.translate(str.maketrans('abcxyz', 'xyzabc')))
    

if __name__ == '__main__':
    # split()
    # endswith()
    # replace()
    # concat()
    # align()
    trim()
    pass
