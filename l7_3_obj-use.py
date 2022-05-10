class Person:
    next_id = 1

    def __init__(self, navn):
        self.personnummer = Person.next_id
        Person.next_id +=1
        self.navn = navn

    def print(self):
        print(vars(self))

klasse = [
    Person("Simon"), 
    Person("Phillip"), 
    Person("Marcus"),
    Person("Hendrik")
]

klasse[1].hårfarve = "rød"
klasse[0].lærer = True
klasse[3].lærer = True

for person in klasse:
    person.print()    