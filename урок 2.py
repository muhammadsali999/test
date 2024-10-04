# """принципы ООП"""
# """gitignore / git rm --cachhed (-r)"""
#
# from урок1 import Car,mers2
#
# #mers2.marks()
#
# class Zavod:
#     name='завод имени Саша '
#     def __init__(self , id ):
#         self.id=id
#
#
#
# '''дочерний класс'''
#
# class Bmw(Car):
#     # name = 'BMW'
#     # def __init__(self,model,year,id ):
#     #     super().__init__(model,year)
#
#         # self.id=id
#
#     def marks(self):
#         print('официальный представитель BMW')
#
# bmw = Bmw('x5' ,2020)
# # bmw.marks()
# # print(Bmw.mro())
# bmw.sayname()


# ПРИНЦИПЫ ООП:НАСЛЕДОВАНИЕ,ПОЛИМОРФИЗМ,инкапсуляция абстракция
# множественное наследование
# gitignore / git rm --cached (-r)
# СУПЕР класс\РОДИТЕЛЬСКИЙ класс
from урок1 import  Car, mers2





class Zavod:
    name = 'Завод имени Артура'
    def __init__(self, id):
        self.id = id


# дочерний класс
class Bmw(Car,Zavod):
    # global name
    def __init__(self,model,year,id):
        super().__init__(model,year)
        Car.__init__(self,model,year)
        Zavod.__init__(self,id)
    def marks(self):
        print('официальный представитель BMW')


bmw = Bmw('x5', 2022,1)
# bmw.marks()
print(Bmw.mro())
# MRO-порядок выполнения методов
bmw.sayname()
