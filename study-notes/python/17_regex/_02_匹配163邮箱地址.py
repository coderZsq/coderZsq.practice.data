import re


def main():
    email = input("请输入一个邮箱地址: ")
    ret = re.match(r"[a-zA-Z0-9]{4,20}@163\.com$", email)
    if ret:
        print("%s 符合要求...." % email)
    else:
        print("%s 不符合要求...." % email)


if __name__ == '__main__':
    main()