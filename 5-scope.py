# Scope

# Global variables are the ones that are defined and declared outside any function and are not specified to any function. They can be used by any part of the program.

# Global variabel
print("-- 1 --")
a = 1

# Global variabel kan læses inde i funktionen
def forsøg1():
  print("inde i funktion: a =",a)

forsøg1()

# lokal variabel virker kun inde i funktionen
print("-- 2 --")
a = 1
print("a =",a)
def forsøg2():
  a = 2
  print("inde i funktion: a =",a)

forsøg2()
# Den globale variabel er uændret
print("a =",a)

print("-- 3 --")
a = 1
print("a =",a)
# Parameter er lokal variabel 
def forsøg3( a ):
  print("inde i funktion: a =",a)
forsøg3(4)
print("a =",a)

# Man kan ændre globale variabler i funktioner 
# Any variable which is changed or created inside of a function is local, if it hasn’t been declared as a global variable.
# (brug nonlocal for ydre namespace)
print("-- 4 --")
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

