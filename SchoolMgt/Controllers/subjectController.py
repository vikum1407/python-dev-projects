from Modules.subject import Subject

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


    def del_subject(self, subID:int):       
        for subject in self.subject_table:
            if subject.getSubjectID() == subID:
                print(self.subject_table.index(subject))
                self.subject_table.remove(subject)

    def edit_subject(self, subID:int):
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