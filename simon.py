# -*- coding: utf-8 -*-
# testing ground

class Test1:
    def __init__(self):
        self.a =1

class Test2(Test1):
    def __init__(self):
        Test1.__init__(self)
        self.b = self.a+1

class Test3(Test2,Test1):
    def __init__(self):
        Test1.__init__(self)
        Test2.__init__(self)
        self.c = 3

o = Test3()
print( vars(o) )



