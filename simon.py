# -*- coding: utf-8 -*-
# testing ground

class Test1:
    def __init__(self):
        self.a =1
        self._d=4
        self.__e=5

class Test2(Test1):
    def __init__(self):
        Test1.__init__(self)
        self.b = self.a+1

class Test3(Test2,Test1):
    def __init__(self):
        Test1.__init__(self)
        Test2.__init__(self)
        self.c = 3

    def __add__(self, o ):
        for k, v in vars( o ).items():
            self.__dict__[k] += v
        return self

    def __sub__(self, o ):
        for k, v in vars( o ).items():
            self.__dict__[k] += v
        return self

o1 = Test3()
o2 = Test3()

print( vars(o1) )

print( vars(o1 + o2))

