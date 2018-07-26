
day = 0

def get_sunday():
    return 'Sunday'

def get_monday():
    return 'Monday'

def get_tuesday():
    return 'Tuesday'

def get_default():
    return 'Unkown'

switcher = {
    0 : get_sunday,
    1 : get_monday,
    2 : get_tuesday
}

day_name = switcher.get(day, get_default)()
print(day_name)

a = [1, 2, 3, 4, 5, 6, 7, 8]
b = [i**2 for i in a if i >= 5]
print (b)

students = {
    'stu1' : 18,
    'stu2' : 20,
    'stu3' : 15
}

b = {value :  key for key, value in students.items()}
print (b)

class Test():
    def __bool__(self):
        print('bool call')
        return False
    def __len__(self):
        print('len call')
        return 8

print(bool(Test()))
print(len(Test()))
