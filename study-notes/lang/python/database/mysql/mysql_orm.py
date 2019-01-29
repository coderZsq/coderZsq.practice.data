from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, Boolean

engine = create_engine('mysql://root:root@localhost:3306/news_test?charset=utf8')
Base = declarative_base()
Session = sessionmaker(bind=engine)

class News(Base):
    __tablename__ = 'news'
    id = Column(Integer, primary_key=True)
    title = Column(String(200), nullable=False)
    content = Column(String(2000), nullable=False)
    types = Column(String(10), nullable=False)
    image = Column(String(300),)
    author = Column(String(20),)
    view_count = Column(Integer)
    create_at = Column(DateTime)
    is_valid = Column(Boolean)

class OrmTest(object):
    def __init__(self):
        self.session = Session()

    def add_one(self):    
        '''新增记录'''
        new_obj = News(
            title = '标题',
            content = '内容',
            types = '百家'
        )
        self.session.add(new_obj)
        self.session.commit()
        return new_obj

    def get_one(self):
        '''查询一条数据'''
        return self.session.query(News).get(1)

    def get_more(self):
        '''查询多条数据'''
        return self.session.query(News).filter_by(is_valid=True)  

    def update_data(self, pk)      :
        '''修改数据'''
        #修改多条数据
        data_list = self.session.query(News).filter_by(is_valid=True)
        for item in data_list:
            item.is_valid = 0
            self.session.add(item)
        self.session.commit()
        #修改单条数据
        # new_obj = self.session.query(News).get(pk)
        # if new_obj:
        #     new_obj.is_valid = 0
        #     self.session.add(new_obj)
        #     self.session.commit()
        #     return True
        # return False

    def delete_data(self, pk):
        '''删除数据'''
        #获取要删除的数据
        new_obj = self.session.query(News).get(pk)
        self.session.delete(new_obj)
        self.session.commit()

def main():
    # News.metadata.create_all(engine)
    obj = OrmTest()
    # rest = obj.add_one()
    # print(rest.id)
    # rest = obj.get_one()
    # if rest:
    #     print('ID:{0}=>{1}'.format(rest.id, rest.title))
    # else:
    #     print('Not exist.')

    # rest = obj.get_more()
    # print(rest.count())
    # for new_obj in rest:
    #     print('ID:{0}=>{1}'.format(new_obj.id, new_obj.title))

    # print(obj.update_data(1))

    obj.delete_data(1)

if __name__ == '__main__':
    main()


