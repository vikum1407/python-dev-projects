class Subject:

    def __init__(self, subjectName:str, subjectID:int):
        self.subjectName = subjectName
        self.subjectID = subjectID

    def setSubjectName(self, subjectName):
        self.SubjectName = subjectName

    def getSubjectName(self):
        return self.subjectName

    def setSubjectID(self, subjectID):
        self.subjectID = subjectID
 
    def getSubjectID(self):
        return self.subjectID
