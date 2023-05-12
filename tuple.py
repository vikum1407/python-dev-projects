# Tuple items are ordered, unchangeable, and allow duplicate values.

stuple = ("apple","orange","banana") #this is called "packing" a tuple
ntuple = (12,23,34,45,67) #this is called "packing" a tuple
btuple = (True, False, True) #this is called "packing" a tuple

mixtuple = ("apple", "banana", 12, True) #this is called "packing" a tuple

print(stuple)
print(ntuple)
print(btuple)
print(mixtuple)

#Accessing tuple

print(stuple[0]) #specific index value
print(stuple[-1]) #specific index value in reverse order

print(stuple[0:2]) #specific index range values

print(ntuple[1:]) #(23, 34, 45, 67) -> specific index values from start value to last value

print(ntuple[:3]) #(12, 23, 34) -> specific index value from given last value to start

# Unpacking tuple:-

(value_0,value_1,value_2) = stuple
print(value_0)
print(value_1)
print(value_2)

(value_0,value_1,*value_2) = ntuple
print(value_0)
print(value_1)
print(value_2) #[34, 45, 67]

#Join tuple:-

newtuple = stuple + ntuple
print(newtuple) #('apple', 'orange', 'banana', 12, 23, 34, 45, 67)

#Tuple Methods:-

stuple = ("apple","orange","banana", "apple")
print(stuple.count("apple"))

print(stuple.index("banana"))


#Looping Tuple:-

for i in range(len(stuple)):
    print(stuple[i])

#check item -
if "banana" in stuple:
    print("Found")
else:
    print("Not Found")

