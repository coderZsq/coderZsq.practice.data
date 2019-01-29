import MySQLdb

class MysqlSearch(object):

    def __init__(self,):
        self.get_conn()

    def get_conn(self):
        try:
            self.conn = MySQLdb.connect(
                host='127.0.0.1',
                user='root',
                passwd='root',
                db='movie',
                port=3306,
                charset='utf8'
            )
        except MySQLdb.Error as e:
             print('Error: %s' % e)

    def close_conn(self):
        try:
            if self.conn:
                #关闭链接
                self.conn.close()
        except MySQLdb.Error as e:
             print('Error: %s' % e)

    def get_one(self):
        #准备SQL
        sql = 'SELECT * FROM `top250` WHERE `year` = %s ORDER BY `rate` DESC;'
        #找到cursor
        cursor = self.conn.cursor()
        #执行SQL
        cursor.execute(sql, ('2013',))\
        #拿到结果
        rest = dict(zip([k[0] for k in cursor.description], cursor.fetchone()))
        #处理数据
        #关闭cursor/链接
        cursor.close()
        self.close_conn()
        return rest

    def get_more(self):
        #准备SQL
        sql = 'SELECT * FROM `top250` WHERE `year` = %s ORDER BY `rate` DESC;'
        #找到cursor
        cursor = self.conn.cursor()
        #执行SQL
        cursor.execute(sql, ('2013',))
        #拿到结果
        rest = [dict(zip([k[0] for k in cursor.description], row)) for row in cursor.fetchall()]
        #处理数据
        #关闭cursor/链接
        cursor.close()
        self.close_conn()
        return rest

    def get_more_by_page(self, page, page_size):
        #准备SQL
        offset = (page - 1) * page_size
        sql = 'SELECT * FROM `top250` WHERE `year` = %s ORDER BY `rate` DESC LIMIT %s, %s;'
        #找到cursor
        cursor = self.conn.cursor()
        #执行SQL
        cursor.execute(sql, ('2013', offset, page_size))
        #拿到结果
        rest = [dict(zip([k[0] for k in cursor.description], row))
                for row in cursor.fetchall()]
        #处理数据
        #关闭cursor/链接
        cursor.close()
        self.close_conn()
        return rest

    def add_one(self):
        try:
            #准备SQL
            sql = (
                "INSERT INTO `top250` (`title`, `year`, `rate`, `url`) VALUE"
                "(%s, %s, %s, %s);"
            )
            #获取链接和cursor
            cursor = self.conn.cursor()
            #执行sql
            #提交数据到数据库
            cursor.execute(sql, ('Castie!', 2018, '10.0',
                             'https://www.github.com/coderzsq'))
            #提交事务
            self.conn.commit()
            #关闭cursor和链接
            cursor.close()
        except:
            print('error')
            self.conn.rollback()
        self.close_conn()

def main():
    obj = MysqlSearch()
    # rest = obj.get_one()
    # print(rest['title'])
    
    # rest = obj.get_more()
    # for item in rest:
    #     print(item)
    #     print('------')

    obj.add_one()

if __name__ == '__main__':
    main()
