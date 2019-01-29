from mongoengine import connect, Document, EmbeddedDocument, DynamicDocument,\
StringField, IntField, FloatField, ListField, EmbeddedDocumentField

connect('students')

SEX_CHOICES = (
    ('male', '男'),
    ('female', '女')
)

class Grade(EmbeddedDocument):
    '''成绩'''
    name = StringField(required=True)
    score = FloatField(required=True)

class Student(DynamicDocument):
    '''学生'''
    name = StringField(max_length=32, required=True)
    age = IntField(required=True)
    sex = StringField(choices=SEX_CHOICES, required=True)
    grade = FloatField()
    address = StringField()
    grades = ListField(EmbeddedDocumentField(Grade))
    # remark = StringField()

    meta = {
        'collection': 'students',
        'ordering': ['-age']
    }

class TestMongoEngine(object):

    def add_one(self):
        '''添加一条数据到数据库'''
        yuwen = Grade(
            name = '语文',
            score = 90
        )
        shuxue = Grade(
            name = '数学',
            score = 100
        )
        stu_obj = Student(
            name = '张三',
            age = 15,
            sex = 'male',
            grades = [yuwen, shuxue]
        )
        stu_obj.remark = 'remark'
        stu_obj.save()
        return stu_obj

    def get_one(self):
        '''查询一条数据'''
        return Student.objects.first()

    def get_more(self):
        '''查询多条数据'''
        return Student.objects.all()

    def get_from_oid(self, oid):
        '''根据ID来获取数据'''
        return Student.objects.filter(pk=oid).first()

    def update(self):
        '''修改数据'''
        #修改所有的男生年龄, 增加10岁
        # return Student.objects.filter(sex='male').update(inc__age=10)
        #修改一条数据
        return Student.objects.filter(sex='male').update_one(inc__age=100)

    def delete(self):
        '''删除数据'''
        #删除一条数据
        # return Student.objects.filter(sex='male').first().delete()
        #删除多条数据
        return Student.objects.filter(sex='male').delete()

def main():
    obj = TestMongoEngine()
    # rest = obj.add_one()
    # print(rest.pk)

    # rest = obj.get_one()
    # print(rest.id)
    # print(rest.name)

    # rows = obj.get_more()
    # for row in rows:
    #     print(row.name)

    # rest = obj.get_from_oid('5b7a7a121e708f58a37f5dd8')
    # if rest:
    #     print(rest.id)
    #     print(rest.name)

    # rest = obj.update()
    # print(rest)

    # rest = obj.delete()
    # print(rest)

if __name__ == '__main__':
    main()
