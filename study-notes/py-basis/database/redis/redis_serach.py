import redis
# r = redis.Redis(host='localhost', port=6379, db=0)

class Base(object):
    def __init__(self):
        self.r = redis.StrictRedis(host='localhost', port=6379, db=0)


class TestString(Base):
    '''
    set -- 设置值
    get -- 获取值
    mset -- 设置多个键值对
    mget -- 获取多个键值对
    append -- 添加字符串
    del -- 删除
    incr/decr -- 增加/减少1
    '''

    def test_set(self):
        '''set -- 设置值'''
        rest = self.r.set('user2', 'Amy')
        print(rest)
        return rest

    def test_get(self):
        '''get -- 获取值'''
        rest = self.r.get('user2')
        print(rest)
        return rest

    def test_mset(self):
        '''mset - - 设置多个键值对'''
        d = {
            'user3' : 'Bob',
            'user4' : 'Bobx'
        }
        rest = self.r.mset(d)
        print(rest)
        return rest

    def test_mget(self):
        '''mget - - 获取多个键值对'''
        l = ['user3', 'user4']
        rest = self.r.mget(l)
        print(rest)
        return rest

    def test_del(self):
        '''del'''
        rest = self.r.delete('user3')
        print(rest)


class TestList(Base):
    '''
    lpush/rpush -- 从左/右插入数据
    lrange -- 获取指定长度的数据
    ltrim -- 截取一定长度的数据
    lpop/rpop -- 移除最左/右的元素并返回
    lpushx/rpushx -- key存在的时候才插入数据, 不存在的时候不做任何处理
    '''

    def test_push(self):
        '''lpush/rpush -- 从左/右插入数据'''
        t = ('Amy', 'Jhon')
        rest = self.r.lpush('l_eat', *t)
        print(rest)
        rest = self.r.lrange('l_eat', 0, -1)
        print(rest)

    def test_pop(self):
        '''lpop/rpop -- 移除最左/右的元素并返回'''
        rest = self.r.lpop('l_eat')
        print(rest)
        rest = self.r.lrange('l_eat', 0, -1)
        print(rest)


class TestSet(Base):
    '''
    sadd/srem -- 添加/删除元素
    sismember -- 判断是否为set的一个元素
    semebers -- 返回该集合的所有成员
    sdiff -- 返回一个集合与其它集合的差异
    sinter -- 返回几个集合的交集
    sunion -- 返回几个集合的并集
    '''
    def test_sadd(self):
        '''sadd -- 添加元素'''
        l = ['Cat', 'Dog']
        rest = self.r.sadd('zoo2', *l)
        print(rest)
        rest = self.r.smembers('zoo2')
        print(rest)

    def test_srem(self):
        '''srem -- 删除元素'''
        rest = self.r.srem('zoo', 'Dog')
        print(rest)
        rest = self.r.smembers('zoo')
        print(rest)

    def test_sinter(self):
        '''sinter -- 返回几个集合的交集'''
        rest = self.r.sinter('zoo', 'zoo2')
        print(rest)

def main():
    # str_obj = TestString()
    # str_obj.test_set()  
    # str_obj.test_get()
    # str_obj.test_mset()
    # str_obj.test_mget()
    # str_obj.test_del()

    # list_obj = TestList()
    # list_obj.test_push()
    # list_obj.test_pop()

    set_obj = TestSet()
    # set_obj.test_sadd()
    # set_obj.test_srem()
    set_obj.test_sinter()

if __name__ == '__main__':
    main()
