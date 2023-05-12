class Myclass:

    #which is always executed when the class is been initiated
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def setName(self, name: str):
        self.name = name

    def getName(self):
        return self.name

    def setAge(self, age: int):
        self.age = age

    def getAge(self):
        return self.age


obj = Myclass("vikum", 32)
print(obj.getName())
print(obj.getAge())

obj.setName("pasindu")
obj.setAge(25)
print(obj.getName())
print(obj.getAge())

obj.name = "kasun"
print(obj.getName())

#Deleting obj parameter
del obj.name
# print(obj.getName()) #AttributeError: 'Myclass' object has no attribute 'name'


#Deleting obj 
del obj
#print(obj.getAge()) #NameError: name 'obj' is not defined




