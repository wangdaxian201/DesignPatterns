#! /bin/env/python
#describe: 实现一下单例模式
#author: wang'yu'hao
#time: 2022/12/19

import threading


class Singleton(object):
    # 定义类变量实例
    __instance = None

    # 线程锁
    __lock = threading.Lock()

    
    def __new__(cls, *args, **kwargs):
        """
        获取单例实例
        """
        # 加锁
        # 如果实例不存在，则创建实例
        with cls.__lock:
            if cls.__instance is None:
                cls.__instance = Singleton(*args, **kwargs)
        return cls.__instance
    
    def __init__(self, name) -> None:

        # 加锁
        with self.__lock:
            self.name = name



if __name__ == '__main__':
    # a = threading.Thread(target=Singleton, args=('a',))
    # b = threading.Thread(target=Singleton, args=('b',))
    # c = threading.Thread(target=Singleton, args=('c',))

    # print(a.start)
    # print(b.start)
    # print(c.start)
    Singleton('a').name
    Singleton('b').name
    Singleton('c').name
    