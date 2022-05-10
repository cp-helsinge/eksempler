class Person:
    next_id = 1

    def __init__(self, navn):
        self.personnummer = Person.next_id
        Person.next_id +=1
        self.navn = navn

    def print(self):
        print(vars(self))

elev = Person("Simon")
elev.adresse = "Kødbyen 7"
elev.print()
    