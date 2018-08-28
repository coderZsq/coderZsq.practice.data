from urllib.request import urlretrieve
import csv
import json
from xml.etree.ElementTree import parse, Element, ElementTree, tostring

# urlretrieve('http://table.finance.yahoo.com/table.csv?s=000001.sz', 'pingan.csv')

def csvrw():
    rf = open('pb_20180808_4.3.2.csv', 'rt', encoding='utf8')
    reader = csv.reader(rf)
    print(reader.__next__())
    # for row in reader: print(row)

    wf = open('pb.csv', 'wt', encoding='utf8')
    writer = csv.writer(wf)
    writer.writerow(['', '商品详情页,3.7.40版本以及以上如果无数据的情况，status返回为0，不在返回非0的错误码',
                     'MallGoodsDetail', 'Response', '', '', '', ''])
    writer.writerow(reader.__next__())                     
    wf.flush()


def jsonrw():
    l = [1, 2, 'abc', {'name': 'Bob', 'age' : 13}]
    print(json.dumps(l))
    d = {'b': None, 'a' : 5, 'c': 'abc'}
    print(json.dumps(d))
    print(json.dumps(l, separators=[',',':']))
    print(json.dumps(d, sort_keys=True))

    l2 = json.loads('[1, 2, "abc", {"name": "Bob", "age": 13}]')
    print(l2[0])
    print(l2[2])
    d2 = json.loads('{"a": 5, "b": null, "c": "abc"}')
    print(d2)
    print(d2['a'])

    with open('demo.json', 'wt', encoding='utf8') as f:
        json.dump(l, f)

def xmlr():
    f = open('demo.xml')
    et = parse(f)
    root = et.getroot()
    print(root)
    print(root.tag)
    print(root.attrib)
    print(root.text)
    print(root.text.strip())
    print(root.getchildren())
    for child in root:
        print(child.get('name'))
    print(root.find('dependencies'))
    print(root.findall('dependencies'))
    print(root.iterfind('dependencies'))
    for e in root.iterfind('dependencies'): print(e.get('name'))
    print(root.iter())
    print(list(root.iter()))
    print(root.iter('outlet'))
    print(list(root.iter('outlet')))
    print(root.findall('dependencies/*'))
    print(root.findall('.//imageView'))
    print(root.findall('.//imageView/..'))
    print(root.findall('.//constraint[@firstItem]'))
    print(root.findall('.//constraint[@firstItem="hNG-5N-PNE"]'))
    print(root.findall('../constraints[constraint]'))
    print(root.findall('../constraints[constraint="5"]'))
    print(root.findall('.//constraint[1]'))
    print(root.findall('.//constraint[2]'))
    print(root.findall('.//constraint[last()]'))
    print(root.findall('.//constraint[last()-1]'))

def xmlw():
    e = Element('Data')
    print(e)
    e.set('name', 'abc')
    print(tostring(e))

if __name__ == '__main__':
    # csvrw()
    # jsonrw()
    # xmlr()
    xmlw()
    pass

