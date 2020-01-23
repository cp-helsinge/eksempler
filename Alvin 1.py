print("hej med dig vad spiser du")
svar_fra_abefjæs=input()
print("FY FOR FANDEN!!!!!!!!!! AD!",svar_fra_abefjæs)
svar=(
  "FY FOR FANDEN!!!!!!!!!! AD!",
  "FANDME LÆKKERT",
  "Nå...øv! Jeg trode det var bits..."
)
i=0
while len(svar_fra_abefjæs) > 0:
  print("hvad spiser du? ")
  svar_fra_abefjæs=input()
  print(svar[i])
  i=i+1