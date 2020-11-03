# lister har en fastsat tal som nøgle, der kaldes et indeks.
liste = ['abe',"bjørn","chinchilla","dromedar"]

print(liste)


liste[3] = "dingo"
print(liste)

for punkt in liste:
  print(punkt)

# Lister kan nogle ekstra ting

thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list") 


thislist.append("orange")
thislist.insert(1, "orange")
thislist.remove("banana")
thislist.pop()
mylist = thislist.copy()

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list3 = list1 + list2


# Method 	Description
# append()	Adds an element at the end of the list
# clear()	Removes all the elements from the list
# copy()	Returns a copy of the list
# count()	Returns the number of elements with the specified value
# extend()	Add the elements of a list (or any iterable), to the end of the current list
# index()	Returns the index of the first element with the specified value
# insert()	Adds an element at the specified position
# pop()	Removes the element at the specified position
# remove()	Removes the first item with the specified value
# reverse()	Reverses the order of the list
# sort()	

# Lykke igennem lister og dictionaries