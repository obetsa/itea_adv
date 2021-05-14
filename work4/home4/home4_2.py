"""2.   Создайте абстрактный класс «Оргтехника», который будет базовым для классов-наследников.
    Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс и т.д.). 
    В базовом классе определите абстрактные методы, общие для приведённых типов. 
    В классах-наследниках реализуйте их, а также добавьте уникальные для каждого
 типа оргтехники функциональные возможности.

 Также создайте класс «Склад», экземпляр которого будет способен принимать в себя объекты техники на хранение.
 Организуйте для него протокол итерации (чтобы объекты вашего склада можно было бы перебирать).
"""
from abc import ABC, abstractmethod
from uuid import uuid4


spisok = []

class BaseOrgtech(ABC):

    # @abstractmethod
    # def name(self):
    #     pass

    @abstractmethod
    def ping(self):
         print("ping: ")

class Printer(BaseOrgtech):
    def __init__(self, t_printer):
        self.id = id
        self.t_printer = t_printer
    
    def ping(self):
        super().ping()
        print("Printer\n")
    
    # def name(self):
    #     print("Printer HP")


class Scanner(BaseOrgtech):
    def __init__(self, t_scanner):
        self.id = id
        self.t_scanner = t_scanner
#     #     self.scan = scan

    def ping(self):
        super().ping()
        print("Scanner\n")


class Xerox(BaseOrgtech):
    def __init__(self, id):
        self.id = id
        # self.t_xerox = t_xerox
# #         self.xero = xero

    def ping(self):
        super().ping()
        print("Xerox")

TYPES_MAPPING = {
    "printer": Printer,
    "scanner": Scanner,
    "xerox": Xerox
}

class Sclad:
    def __init__(self, type, *args, **kwargs):
        self.type = type
        self.id = uuid4()
        class_of_tech = TYPES_MAPPING[type]
        return class_of_tech(id=self.id, *args, **kwargs)

    def save_item(self):
        spisok.append(self)
        





# p = Printer()
# p.ping()
# # p.name()
# s = Scanner()
# s.ping()
# x = Xerox()
# x.ping()

a = Sclad(type='xerox')
print(a)

