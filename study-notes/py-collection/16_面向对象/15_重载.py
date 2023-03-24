# class Person:
#     # def leave(self, year, month, day):
#     #     print(self, 1, year, month, day)
#
#     def leave(self, date):
#         print(self, 2, date)
#
#
# p = Person()
# p.leave('2001-11-17')
# p.leave(2001, 11, 17)

class Person:
    def leave(self, date=None, year=None, month=None, day=None):
        print(self, date, year, month, day)


p = Person()
p.leave('2001-11-17')
p.leave(year=2001, month=11, day=17)
