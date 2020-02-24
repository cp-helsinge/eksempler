# En lykke der beregner fibronacci tal
# beregning: Et hvert tal, er lig med summen af de to forudgående tal, startende med 1.
# Eksempel: 1 1 2 3 5 8 13 

a=1
b=1
for n in range(1,10):
  print(a, end =" "),
  c=a+b
  a=b
  b=c
print("")





