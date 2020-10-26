# lokal variabel virker kun inde i funktionen
a = 1
print("a =",a)
def forsøg2():
  a = 2
  print("inde i funktion: a =",a)

forsøg2()
# Den globale variabel er uændret
print("a =",a)

