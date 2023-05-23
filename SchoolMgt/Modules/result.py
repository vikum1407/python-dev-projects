class Result:

    def __init__(self, student:int, subject:int, marks:int):
        self.marks = marks
        self.student = student
        self.subject = subject

    def setStudent(self, student):
        self.student = student

    def getStudent(self):
        return self.student

    def setSubject(self, subject):
        self.subject = subject
 
    def getSubject(self):
        return self.subject

    def setMarks(self, marks):
        self.marks = marks
 
    def getMarks(self):
        return self.marks