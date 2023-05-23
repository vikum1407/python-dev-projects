from Modules.student import Student

class crudStudent(Student): 

    student_table = []

    def __init__(self):
        pass

    def add_student(self, stdID:int, stdName:str):
        self.student_table.append(Student(stdName, stdID))

    def get_student_value(self, stdID:int):
        for student in self.student_table:
            if student.getStudentID() == stdID:
                return student
        return -1

    def get_student_index(self, stdID:int):
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
                return 1
        return -1

    def edit_student(self, stdID:int, stdName:str):
        for student in self.student_table:
            if student.getStudentID() == stdID:
                self.student_table[self.student_table.index(student)] = Student(stdName, stdID)
                return 1
        return -1

   
