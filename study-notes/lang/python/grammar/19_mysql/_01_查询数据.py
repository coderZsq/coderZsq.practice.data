from pymysql import connect


class JD(object):
    def __init__(self):
        pass

    def show_all_items(self):
        conn = connect(host="localhost", port=3306, user="root", password="root", database="jing_dong", charset="utf8")
        cursor = conn.cursor()
        sql = "select * from goods"
        cursor.execute(sql)
        for temp in cursor.fetchall():
            print(temp)
        cursor.close()
        conn.close()

    def show_cates(self):
        conn = connect(host="localhost", port=3306, user="root", password="root", database="jing_dong", charset="utf8")
        cursor = conn.cursor()
        sql = "select name from goods_cates"
        cursor.execute(sql)
        for temp in cursor.fetchall():
            print(temp)
        cursor.close()
        conn.close()

    def run(self):
        while True:
            print("------京东商城------")
            print("1: 所有的商品")
            print("2: 所有的商品分类")
            print("3: 所有的商品品牌分类")
            num = input("请输入功能对应的序号: ")

            if num == "1":
                self.show_all_items()
            elif num == "2":
                pass
            elif num == "3":
                pass
            else:
                print("输入有误, 重新输入....")


def main():
    jd = JD()
    jd.run()


if __name__ == '__main__':
    main()