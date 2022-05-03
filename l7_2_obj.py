class Person:
    next_id = 1

    def __init__(self, navn):
        self.personnummer = Person.next_id
        Person.next_id +=1
        self.navn = navn

    def print(self):
        print(vars(self))

elev1 = Person("Simon")
elev2 = Person("Simon")
lærer1 = Person("Gurusen")

elev1.adresse = "Kødbyen 7"

elev1.print()
elev2.print()

    