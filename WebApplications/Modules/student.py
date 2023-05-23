class Student:

    def __init__(self, studentName:str, studentID:int):
        self.studentName = studentName
        self.studentID = studentID

    def setStudentName(self, studentName):
        self.studentName = studentName

    def getStudentName(self):
        return self.studentName

    def setStudentID(self, studentID):
        self.studentID = studentID
 
    def getStudentID(self):
        return self.studentID