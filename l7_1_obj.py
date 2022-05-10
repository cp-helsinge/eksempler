class Person:
    def __init__(self, navn):
        self.navn = navn

    def print(self):
        print("Hej, mit navn er",self.navn)

elev = Person("Simon")
elev.print()

elev2 = Person("Phillip")
elev2.print()