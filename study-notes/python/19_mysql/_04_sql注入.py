from pymysql import connect


class JD(object):
    def __init__(self):
        self.conn = connect(host="localhost", port=3306, user="root", password="root", database="jing_dong", charset="utf8")
        self.cursor = self.conn.cursor()

    def __del__(self):
        self.cursor.close()
        self.conn.close()

    def execute_sql(self, sql):
        self.cursor.execute(sql)
        for temp in self.cursor.fetchall():
            print(temp)

    def show_all_items(self):
        sql = "select * from goods;"
        self.execute_sql(sql)

    def show_cates(self):
        sql = "select name from goods_cates;"
        self.execute_sql(sql)

    def show_brands(self):
        sql = "select name from goods_brands;"
        self.execute_sql(sql)

    def add_brands(self):
        item_name = input("输入新商品分类的名称: ")
        sql = """insert into goods_brands (name) values("%s");""" % item_name
        self.cursor.execute(sql)
        self.conn.commit()

    def get_info_by_name(self):
        find_name = input("请输入要查询的商品的名字: ")
        sql = """select * from goods where name='%s';""" % find_name
        self.execute_sql(sql)

    @staticmethod
    def print_menu():
        print("------京东商城------")
        print("1: 所有的商品")
        print("2: 所有的商品分类")
        print("3: 所有的商品品牌分类")
        print("4: 添加一个商品分类")
        print("5: 根据名字查询一个商品")
        return input("请输入功能对应的序号: ")

    def run(self):
        while True:
            num = self.print_menu()
            if num == "1":
                self.show_all_items()
            elif num == "2":
                self.show_cates()
            elif num == "3":
                self.show_brands()
            elif num == "4":
                self.add_brands()
            elif num == "5":
                self.get_info_by_name()
            else:
                print("输入有误, 重新输入....")


def main():
    jd = JD()
    jd.run()


if __name__ == '__main__':
    main()