# brug google til at forstå "python string format" metoden (3wschool)
# lav et program der kan:
#   indlæse tre tal
#   udskrive dem i en kolonne, højrejusteret (align) og med to decimaler (fix point)
n = list()
l = 1
for i in range(3):
    #input float
    n.append(float(input('Skriv ' + str(i+1) + '.tal: ')))
    # find the longest integer part
    i,d = divmod(n[i],1)
    il = len(str(i))
    if il > l: 
        l = il

# Formater kolonne (husk at der kan være fortegn)
kolonne = '{:>' + str(l+2) + '.2f}'
for i in n:
    print(kolonne.format(i))
