from Modules.student import Student

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
