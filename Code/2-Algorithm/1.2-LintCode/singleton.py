#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'Windrivder'

# -----------------------------------------------------------------------------

# module singleton
class Module_Singleton(object):

    def foo(self):
        pass

# module in the import for the first time, will generate the pyc file, when the second import, will direct load. Pyc file, rather than execution module code again. Therefore, we need to define the relevant functions and data in a module, you can get a singleton.
module_singleton = Module_Singleton()

# -----------------------------------------------------------------------------

# use __new__
class New_Singleton(object):

    _instance = None
    def __new__(cls, *args, **kw):
        if not cls._instance:
            cls._instance = super(New_Singleton, cls).__new__(cls, *args, **kw)
        return cls._instance


class MyClass(New_Singleton):
    a = 1

# -----------------------------------------------------------------------------

# use decorator
from functools import wraps

def decorator_singleton(cls):
    instances = {}
    @wraps(cls)
    def getinstance(*args, **kw):
        if cls not in instances:
            instances[cls] = cls(*args, **kw)
        return instances[cls]
    return getinstance

@decorator_singleton
class My_Test(object):
    a = 1

# -----------------------------------------------------------------------------

# use metaclass
class Metaclass_Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class My_Test3(metaclass=Metaclass_Singleton):
    pass

# -----------------------------------------------------------------------------

# 实例的唯一性并不是重要的，我们应该关注的是实例的状态，只要所有的实例共享状态，行为一致，那就达到了单例的目的
class Borg:
    _shared_state = {}
    def __init__(self):
        self.__dict__ = self._shared_state


if __name__ == '__main__':

    one = MyClass()
    two = MyClass()
    print(one==two)
    print(one is two)
    print(id(one), id(two))
