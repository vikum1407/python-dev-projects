#A dictionary is a collection which is ordered*, changeable and do not allow duplicates.

# Dictionary items are presented in key:value pairs, and can be referred to by using the key name.

fdict = {"type":"sedan","brand":"bmw","year":1990,"active":True}

print(fdict)

#Retrieve data:-

print(fdict["type"])

# Changing data:-

fdict["brand"]="toyota"
print(fdict)

# Removing data:-

fdict.pop("brand")
print(fdict)

# Adding :-

fdict["country"]="UK"
print(fdict)

# Looping:-

for k,v in fdict.items():
    print(k)
    print(v)

for key in fdict:
    print(fdict[key])


# collection of data dictionary:-

dictList = [fdict,fdict]

print(dictList)
print(dictList[1])


