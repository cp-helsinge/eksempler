# definer en funktion
def plus(a, b):
  c = a + b
  return c

# Brug funktionen
for n in range(1,10):
  print( plus(10, n) )


# Lav noget 
def tabel( mul ):
  for n in range( 1, 11):
    print(n,"*",mul,"=", n*mul)

tabel(7) 
tabel(17) 