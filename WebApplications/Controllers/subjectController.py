from Modules.subject import Subject

class crudSubject(Subject):
    subject_table = []

    def __init__(self):
        pass

    def add_subject(self, subID:int, subName:str):
        self.subject_table.append(Subject(subName, subID))

    def get_subject_value(self, subID:int):
        for subject in self.subject_table:
            if subject.getSubjectID() == subID:
                return subject
        return -1

    def get_subject_index(self, subID:int):
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
                return 1
        return -1

    def edit_subject(self, subID:int, subName:str):
        for subject in self.subject_table:
            if subject.getSubjectID() == subID:
                self.subject_table[self.subject_table.index(subject)] = Subject(subName, subID)
                return 1
        return -1

    