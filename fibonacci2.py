# Omsæt specialiseret formel til algoritme, for hurtig beregning af Fibonacci tal.
# (med brug af closed form funktion)
#
# F(n) = 1/sqet(5) * ((1+sqrt(5)) /2 ) ** n - 1/sqet(5) * ((1-sqrt(5)) /2 ) ** n
#
# Se forklaring here: http://mathonline.wikidot.com/a-closed-form-of-the-fibonacci-sequence
# Mere pædagogosk forklaring her: https://www.quora.com/What-is-something-that-is-trivial-to-a-mathematician-but-would-amaze-a-layperson/answer/Nish-Jayram

import math

# Tildel værdier til nogle "magiske" konstanter (For hurtigere beregning)
sqrt5 = math.sqrt(5)
factor = 1 / sqrt5;
k1 = (1 + sqrt5) / 2
k2 = (1 - sqrt5) / 2

def fibonacci(n):
  f = factor  * k1 ** n - factor * k2 ** n  # Sammensæt formel
  return round(f) # Afrund, for at fjerne afrundingsfejl

for n in range(1,100):
  print(fibonacci(n))





