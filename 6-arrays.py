# lister og ordbøger (Arrays)

# der er to slags array i python: 
# lister, der har et numerink index og dictionaries, der kan have tekst eller tal som index.


# definition
print("-- 1 --")
dictionary = {
  'dyr': "abe", 
  'bil': "volvo",
  'navn': "børge",
}
print(dictionary)

# ændre
print("-- 2 --")
dictionary["dyr"] = "dingo"
dictionary["bil"] = None

print(dictionary)



liste = ["abe","bjørn","chinchilla","dromedar"]

print(liste)


print("-- 2 --")
liste[3] = "dingo"
print(liste)


# Lykke igennem lister og dictionaries