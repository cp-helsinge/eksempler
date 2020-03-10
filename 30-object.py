# -*- coding: utf-8 -*-
# Objekter

# Terminologi: klasser, objekter, der indeholder variabler og funktioner.

class Test1:
    def __init__(self): # Constructor function
        print("initialiserer Test1")
        self.a = 1    # Public
        self._d = 4   # Protected
        self.__e = 5  # Private

# Nedarvning
class Test2(Test1): # Arver fra Test1
    def __init__(self):
        print("initialiserer Test2")
        Test1.__init__(self) # konstruere Test1 og sammensmelter med denne
        self.b = self.a + 1

# Nedarvning af flere classer
class Test3(Test2,Test1):
    def __init__(self):
        print("initialiserer Test3")
        Test1.__init__(self)
        Test2.__init__(self)
        self.c = 3


    # Overloading
    def __add__(self, o ):
        for k, v in vars( o ).items():
            self.__dict__[k] += v
        return self

    def __sub__(self, o ):
        for k, v in vars( o ).items():
            self.__dict__[k] -= v
        return self

o1 = Test3()
o2 = Test3()

print( vars( o1 ) )

print( vars( o1 + o2 ))


