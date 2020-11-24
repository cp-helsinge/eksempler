class Bil:
    def __init__(self,farve):
        self.farve = farve
        self.hjulstørrelse = 16

    def udskriv(self):
        print(self.farve, self.hjulstørrelse)



bil = Bil('rød')

bil.udskriv()
