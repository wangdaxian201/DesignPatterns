#! /bin/env/python
#describe: 实现一下代理模式
#author: wang'yu'hao
#time: 2022/12/19

# 实现代理模式
from abc import ABC, abstractmethod
class AbstractSubject(ABC):
    @abstractmethod
    def request(self):
        pass


class RealSubject(AbstractSubject):
    def request(self):
        print("RealSubject request")


class Proxy(AbstractSubject):
    def __init__(self, real_subject):
        self.real_subject = real_subject

    def request(self):
        print("Proxy request")
        self.real_subject.request()

# 实现动态代理
def create_proxy(subject):
    class Proxy(subject):
        def request(self):
            print("Proxy request")
            subject.request()

    return Proxy()



if __name__ == "__main__":
    proxy = create_proxy(RealSubject)
    proxy.request()
