# Scope

# Global variables are the ones that are defined and declared outside any function and are not specified to any function. They can be used by any part of the program.

# Global variabel
print("-- 1 --")
a = 1

# Global variabel kan læses inde i funktionen
def forsøg1():
  print("inde i funktion: a =",a)

forsøg1()
