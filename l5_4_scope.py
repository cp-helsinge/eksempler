# Man kan ændre globale variabler i funktioner 
# Any variable which is changed or created inside of a function is local, if it hasn’t been declared as a global variable.
# (brug nonlocal for ydre namespace)
a = 1
b = 2
print("a =",a)
print("b =",b)
# Parameter er lokal variabel 
def forsøg4( a ):
  global b
  a = a + 10
  b = b + 10
  print("inde i funktion: a =",a)
  print("inde i funktion: b =",b)

forsøg4(4)
print("a =",a)
print("b =",b)

