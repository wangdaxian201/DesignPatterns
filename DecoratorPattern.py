#! /bin/env/python
#describe: 实现装饰者模式
#author: wang'yu'hao
#time: 2022/12/19

from abc import ABCMeta, abstractmethod


class Composition(metaclass=ABCMeta):
    @abstractmethod
    def operation(self):
        pass


class ConcreteComposition(Composition):
    def operation(self):
        print("ConcreteComposition operation")  # 此处的operation是抽象方法


class Decorator(Composition):
    def __init__(self, composition): 
        self.composition = composition

    def operation(self):
        self.composition.operation()


class Decorator1(Decorator):
    def operation(self):
        d = Decorator(self.composition)
        d.operation()
        print("Decorator1 operation")


class Decorator2(Decorator):
    def operation(self):
        d = Decorator(self.composition)
        d.operation()
        print("Decorator2 operation") 


if __name__ == '__main__':
    composition = ConcreteComposition()
    decorator1 = Decorator1(composition)
    decorator2 = Decorator2(decorator1)
    decorator2.operation()