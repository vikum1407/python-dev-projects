# A set is a collection which is unordered, unchangeable*, and unindexed.
# Duplicate not allowed

#Define set:-

sSet = {"apple","banana","kiwi"}
nSet = {32,43,54,65,77,88}
bSet = {True, True, False}
mixSet = {"apple", 34, True, 56, "banana"}

print(sSet)
print(nSet)
print(bSet)
print(mixSet)

#Access Set:-

#print(sSet[1]) #Error (can't call with index)

for i in sSet:
    print(i)

#Check elements:-

print("apple" in sSet) #True


#Add item to set:-

sSet.add("orange")
print(sSet) #{'orange', 'apple', 'banana', 'kiwi'}


#Update set :-

newSet = {"volvo","landrover","toyota","bmw"}

sSet.update(newSet)
print(sSet) #{'banana', 'volvo', 'kiwi', 'orange', 'apple', 'bmw', 'landrover', 'toyota'}


#Remove Set:-

sSet.remove("banana") #remove only selected element
print(sSet)

sSet.discard("toyota") #remove only selected element
print(sSet)

sSet.pop() #removing first element
print(sSet)

sSet.clear() #removing all elements
print(sSet)

del sSet # delete set
#print(sSet)

#Join two sets:-
"""
difference()	Returns a set containing the difference between two or more sets
difference_update()	Removes the items in this set that are also included in another, specified set
intersection()	Returns a set, that is the intersection of two other sets
intersection_update()	Removes the items in this set that are not present in other, specified set(s)
isdisjoint()	Returns whether two sets have a intersection or not
issubset()	Returns whether another set contains this set or not
issuperset()	Returns whether this set contains another set or not

symmetric_difference()	Returns a set with the symmetric differences of two sets
symmetric_difference_update()	inserts the symmetric differences from this set and another
union()	Return a set containing the union of sets
"""

