# Brug af filer

# Skriv en tekst ned i en fil og lok den
# Læd tekst fra filen igen og skriv den på skærmen

data = "Husk at lukke lågen når du går ud"
with open("gemte_data.txt", "w") as datafil:
  datafil.write(data)

# Læs data og skriv dem på skærmen
def file_get(file_name):
  with open(file_name, "r") as datafil:
    data = datafil.read()
    return data 

print("Write: ",file_get("gemte_data.txt"))

# Ekstra
#   append 
data = ". Ellers løber hunden ud."
with open("gemte_data.txt", "a") as datafil:
  datafil.write(data)

print("Append:",file_get("gemte_data.txt"))

#   read/write seek, tell
data = "katten"
with open("gemte_data.txt", "r+") as datafil:
  datafil.seek(52)
  datafil.write(data)

print("Seek:  ",file_get("gemte_data.txt"))
