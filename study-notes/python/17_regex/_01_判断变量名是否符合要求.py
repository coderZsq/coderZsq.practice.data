import re


def main():
    names = ["age", "_age", "1age", "age1", "a_age", "age_1_", "age!", "a#123", "_________"]
    for name in names:
        # ret = re.match(r"[a-zA-Z_][a-zA-Z0-9_]*", name)
        # ret = re.match(r"[a-zA-Z_][a-zA-Z0-9_]*$", name)
        ret = re.match(r"^[a-zA-Z_][a-zA-Z0-9_]*$", name)
        if ret:
            print("变量名:%s 符合要求.... 通过正则匹配出来的数据是:%s" % (name, ret.group()))
        else:
            print("变量名:%s 不符合要求...." % name)


if __name__ == '__main__':
    main()