class Subject:

    def __init__(self, subjectName:str, subjectID:int):
        self.subjectName = subjectName
        self.subjectID = subjectID

    def setSubjectName(self, subjectName):
        self.SubjectName = SubjectName

    def getSubjectName(self):
        return self.subjectName

    def setSubjectID(self, subjectID):
        self.subjectID = subjectID
 
    def getSubjectID(self):
        return self.subjectID





class Student(Subject):

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



class Result(Student):

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



# Students adding, updating, retriving and removing from the dictionary

class crudStudent(Student): 

    student_table = []

    def __init__(self):
        pass

    def add_student(self, stdID:int, stdName:str):
        self.student_table.append(Student(stdName, stdID))

    def get_student(self, stdID:int):
        for student in self.student_table:
            if student.getStudentID() == stdID:
                print(student.getStudentID(), student.getStudentName())
                return self.student_table.index(student)
        return -1


    def del_student(self, stdID):
        for student in self.student_table:
            if student.getStudentID() == stdID:
                print(self.student_table.index(student))
                self.student_table.remove(student)

    def edit_student(self, stdID):
        for student in self.student_table:
            if student.getStudentID() == stdID:
                stdID = int(input("Student ID: "))
                stdName = input("Student Name: ")
                self.student_table[self.student_table.index(student)] = Student(stdName, stdID)

    def controller(self):
        while (True):
            print("****************************")
            print(" Welcome To ABC University  ")
            print("============================")
            print("        Student Data        ")
            print("****************************")
            print(" 1. Press A for Add Student ")
            print(" 2. Press B for Get Student ")
            print(" 3. Press C for Del Student ")
            print(" 4. Press D for Edit Student")
            print(" 5. Press Q for Exit        ")
            print("****************************")
            choice = input("Enter Your Choice: ")
            match choice:
                case "A":
                    stdID = int(input("Enter Student ID: "))
                    stdName = input("Enter Student Name: ")
                    self.add_student(stdID, stdName)
                case "B":
                    stdID = int(input("Enter Student ID: "))
                    self.get_student(stdID)
                case "C":
                    stdID = int(input("Enter Student ID: "))
                    self.del_student(stdID)
                case "D":
                    stdID = int(input("Enter Student ID: "))
                    self.edit_student(stdID)
                case "Q":
                    break



class crudSubject(Subject):
    subject_table = []

    def __init__(self):
        pass

    def add_subject(self, subID:int, subName:str):
        self.subject_table.append(Subject(subName, subID))

    def get_subject(self, subID:int):
        for subject in self.subject_table:
            if subject.getSubjectID() == subID:
                print(subject.getSubjectID(), subject.getSubjectName())
                return self.subject_table.index(subject)
        return -1
    

    def get_subject_name(self, index:int):
        return self.subject_table[index].getSubjectName()


    def del_subject(self, subID):       
        for subject in self.subject_table:
            if subject.getSubjectID() == subID:
                print(self.subject_table.index(subject))
                self.subject_table.remove(subject)

    def edit_subject(self, subID):
        for subject in self.subject_table:
            if subject.getSubjectID() == subID:
                subID = int(input("Subject ID: "))
                subName = input("Subject Name: ")
                self.subject_table[self.subject_table.index(subject)] = Subject(subName, subID)

    def controller(self):
        while (True):
            print("****************************")
            print(" Welcome To ABC University  ")
            print("============================")
            print("        Subject Data        ")
            print("****************************")
            print(" 1. Press A for Add Subject ")
            print(" 2. Press B for Get Subject ")
            print(" 3. Press C for Del Subject ")
            print(" 4. Press D for Edit Subject")
            print(" 5. Press Q for Exit        ")
            print("****************************")
            choice = input("Enter Your Choice: ")
            match choice:
                case "A":
                    subID = int(input("Enter Subject ID: "))
                    subName = input("Enter Subject Name: ")
                    self.add_subject(subID, subName)
                case "B":
                    subID = int(input("Enter Subject ID: "))
                    self.get_subject(subID)
                case "C":
                    subID = int(input("Enetr Subject ID: "))
                    self.del_subject(subID)
                case "D":
                    subID = int(input("Enter Subject ID: "))
                    self.edit_subject(subID)
                case "Q":
                    break


class crudResult:

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



while (True):
    print("*********************************")
    print("    Welcome To ABC University    ")
    print("=================================")
    print("      Student Management         ")
    print("*********************************")
    print(" 1. Press A for Student Records  ")
    print(" 2. Press B for Subject Records  ")
    print(" 3. Press C for Result Records   ")
    print(" 5. Press Q for Exit             ")
    print("*********************************")
    choice = input("Enter Your Choice:      ")
    match choice:
        case "A":
            crudStudent().controller()
        case "B":
            crudSubject().controller()
        case "C":
            crudResult().controller()
        case "Q":
            break

   

# interfaceStudent = crudStudent()
# interfaceStudent.add_student(1000, "Vikum")
# interfaceStudent.add_student(1001, "Pasindu")
# interfaceStudent.add_student(1002, "Kasun")
# interfaceStudent.add_student(1003, "Namal")


# interfaceSubject = crudSubject()
# interfaceSubject.add_subject(1000, "Maths")
# interfaceSubject.add_subject(1001, "Music")
# interfaceSubject.add_subject(1002, "Social")
# interfaceSubject.add_subject(1003, "Science")

# interfacecrudResult = crudResult()
# interfacecrudResult.controller()



    












