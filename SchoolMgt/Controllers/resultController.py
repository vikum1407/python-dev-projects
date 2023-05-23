from .studentController import crudStudent
from .subjectController import crudSubject
from Modules.result import Result

class crudResult(Result):

    result_table = []

    def __init__(self):
        pass

    def add_result(self, stdID, subID):    
        if stdID > -1 and subID > -1:
            mark = int(input("Mark: "))
            self.result_table.append(Result(stdID, subID, mark))
            print(stdID, subID, mark)
        else:
            print("invalid_stundetid_or_subjectid")

    def get_result(self, stdID):
        total = 0
        average = 0
        for result in self.result_table:
            if result.getStudent() == stdID:
                total += result.getMarks()
                average = total/len(crudSubject().subject_table)
                print(crudSubject().get_subject_name(result.getSubject()), result.getMarks())
        print("Total Marks: ", total)
        print("Average Marks: ", average)


    def del_result(self, stdID, subID):
        if stdID > -1 and subID > -1:
            for result in self.result_table:
                if stdID == result.getStudent() and subID == result.getSubject(): 
                    print(self.result_table.index(result))
                    self.result_table.remove(result)
                    break

    def edit_result(self, stdID, subID):
        for result in self.result_table:
            if stdID == result.getStudent() and subID == result.getSubject():
                mark = int(input("Mark: "))
                self.result_table[self.result_table.index(result)] = Result(stdID, subID, mark)
                print(stdID, subID, mark)
                break

    def marks_total(self):
        stdID = int(input("Student ID: "))
        for student in self.student_table:
            if student.getStudentID() == stdID:
                total = sum(self.result_table)

    def marks_average(self):
        pass

    def controller(self):
        while (True):
            print("****************************")
            print(" Welcome To ABC University  ")
            print("============================")
            print("       Exam Result          ")
            print("****************************")
            print(" 1. Press A for Add Marks   ")
            print(" 2. Press B for Get Marks   ")
            print(" 3. Press C for Del Marks   ")
            print(" 4. Press D for Edit Marks  ")
            print(" 5. Press Q for Exit        ")
            print("****************************")
            choice = input("Enter Your Choice: ")
            match choice:
                case "A":
                    stdID = crudStudent().get_student(int(input("Student ID: ")))
                    subID = crudSubject().get_subject(int(input("Subject ID: ")))
                    self.add_result(stdID, subID)
                case "B":
                    stdID = crudStudent().get_student(int(input("Student ID: ")))
                    self.get_result(stdID)
                case "C":
                    stdID = int(input("Student ID: "))
                    self.del_result(stdID)
                case "D":
                    stdID = int(input("Student ID: "))
                    self.edit_result(stdID)
                case "Q":
                    break