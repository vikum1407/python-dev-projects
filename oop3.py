class Human:

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


#Employee class inherit from Human class
class Employee(Human):
    pass




objEmp = Employee("piku", 32)
print(objEmp.getName())


class Student(Human):

    def __init__(self, name: str, age: int, school: str, year: int):
        super().__init__(name, age)
        self.school = school
        self.year = year




objStd = Student("siku", 25, "bombuwala MV", 2007)
print(objStd.school)
print(objStd.getName())



    



