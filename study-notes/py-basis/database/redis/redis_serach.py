import redis
# r = redis.Redis(host='localhost', port=6379, db=0)

class TestString(object):
    '''
    set -- 设置值
    get -- 获取值
    mset -- 设置多个键值对
    mget -- 获取多个键值对
    append -- 添加字符串
    del -- 删除
    incr/decr -- 增加/减少1
    '''

    def __init__(self):
        self.r = redis.StrictRedis(host='localhost', port=6379, db=0)

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

class TestList(object):
    '''
    lpush/rpush -- 从左/右插入数据
    lrange -- 获取指定长度的数据
    ltrim -- 截取一定长度的数据
    lpop/rpop -- 移除最左/右的元素并返回
    lpushx/rpushx -- key存在的时候才插入数据, 不存在的时候不做任何处理
    '''

    def __init__(self):
        self.r = redis.StrictRedis(host='localhost', port=6379, db=0)

    def test_push(self):
        pass

def main():
    # str_obj = TestString()
    # str_obj.test_set()  
    # str_obj.test_get()
    # str_obj.test_mset()
    # str_obj.test_mget()
    # str_obj.test_del()

if __name__ == '__main__':
    main()
