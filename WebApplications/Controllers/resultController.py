from .studentController import crudStudent
from .subjectController import crudSubject
from Modules.result import Result

class crudResult(Result):

    result_table = []

    def __init__(self):
        pass

    def add_result(self, stdID:int, subID:int, mark:int):    
        if stdID > -1 and subID > -1:
            #mark = int(input("Mark: "))
            self.result_table.append(Result(stdID, subID, mark))
            print(stdID, subID, mark)
        else:
            print("invalid_stundetid_or_subjectid")

    def get_result_value(self, subID:int):
        for result in self.result_table:
            if result.getStudent() == subID:
                return result
        return -1

    def get_result_index(self, subID:int):
        for result in self.result_table:
            if result.getStudent() == subID:
                print(result.getStudent(), result.getSubject(), result.getMarks())
                return self.result_table.index(result)
        return -1

    def get_result(self, stdID):
        total = 0
        average = 0
        for result in self.result_table:
            if result.getStudent() == stdID:
                total += result.getMarks()
                average = total/len(crudSubject().subject_table)
                #print(crudSubject().get_subject_name(result.getSubject()), result.getMarks())
                return crudSubject().get_subject_name(result.getSubject()), result.getMarks()
        #print("Total Marks: ", total)
        #print("Average Marks: ", average)


    def del_result(self, stdID, subID):
        if stdID > -1 and subID > -1:
            for result in self.result_table:
                if stdID == result.getStudent() and subID == result.getSubject(): 
                    #print(self.result_table.index(result))
                    self.result_table.remove(result)
                    return 1
            return -1

    def edit_result(self, stdID:int, subID:int, mark:int):
        for result in self.result_table:
            if stdID == result.getStudent() and subID == result.getSubject():
                #mark = int(input("Mark: "))
                self.result_table[self.result_table.index(result)] = Result(stdID, subID, mark)
                return 1
                #print(stdID, subID, mark)
        return -1

    def marks_total(self):
        stdID = int(input("Student ID: "))
        for student in self.student_table:
            if student.getStudentID() == stdID:
                total = sum(self.result_table)

    def marks_average(self):
        pass

    