#! /bin/env/python
#describe: 实现一下抽象工厂模式
#author: wang'yu'hao
#time: 2017/12/12

import abc


class AbstractFactory(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def create_product_a(self):
        pass

    @abc.abstractmethod
    def create_product_b(self):
        pass


class AbstractProductA(object):
    __metaclass__ = abc.ABCMeta
    @abc.abstractmethod
    def operation(self):
        pass


class AbstractProductB(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def operation(self):
        pass


class ConcreteFactory1(AbstractFactory):
    def create_product_a(self):
        return ConcreteProductA1()

    def create_product_b(self):
        return ConcreteProductB1()


class ConcreteFactory2(AbstractFactory):
    def create_product_a(self): 
        return ConcreteProductA2()

    def create_product_b(self):
        return ConcreteProductB2()




class ConcreteProductA1(AbstractProductA):
    def operation(self):
        print("ConcreteProductA1")


class ConcreteProductA2(AbstractProductA):
    def operation(self):
        print("ConcreteProductA2")


class ConcreteProductB1(AbstractProductB):
    def operation(self):
        print("ConcreteProductB1")


class ConcreteProductB2(AbstractProductB):
    def operation(self):   
        print("ConcreteProductB2")


class Client(object):
    def __init__(self):
        self.factory = ConcreteFactory1()

    def client(self):
        self.product_a = self.factory.create_product_a()
        self.product_b = self.factory.create_product_b()
        self.product_a.operation()
        self.product_b.operation()


if __name__ == '__main__':
    client = Client()
    client.client()
