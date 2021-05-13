"""2. Создайте абстрактный класс «Оргтехника», который будет базовым для классов-наследников.
 Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс и т.д.). В базовом классе определите абстрактные
 методы, общие для приведённых типов. В классах-наследниках реализуйте их, а также добавьте уникальные для каждого
 типа оргтехники функциональные возможности.
 Также создайте класс «Склад», экземпляр которого будет способен принимать в себя объекты техники на хранение.
 Организуйте для него протокол итерации (чтобы объекты вашего склада можно было бы перебирать).
"""
from abc import ABC, abstractmethod


class BaseOrgtech(ABC):

    @abstractmethod
    def ping(self):
        pass

class Printer(BaseOrgtech):
    def __init__(self):
        self.t_printer = t_printer
        self.printing = printing

class Scanner(BaseOrgtech):
    def __init__(self):
        self.t_scanner = t_scanner
        self.scan = scan

class Xerox(BaseOrgtech):
    def __init__(self):
        self.t_xerox = t_xerox
        self.xero = xero


class Sclad()
 
