class School:

    stdList=[]
    dic={}

    def add_data_to_dict(self):
        while True:
            stdID = input("StudentID: ")
            maths = input("Maths Result: ")
            science = input("Science Result: ")
            music = input("Music Result: ")
            english = input("English Result: ")
            social = input("Social Result: ")
            dic = {"StudentID": stdID, "Maths": maths, "Science": science, "Music": music, "English": english,
                   "Social": social}
            self.stdList.append(dic)
            print("press 'yes' tfor another poll or press 'quit' anytime to exit:")
            anotherPoll = input()
            if anotherPoll == "quit":
                break
#        print(self.stdList)

    
    def retrieve(self):
        self.add_data_to_dict()
        print(self.stdList)


    def removeStd(self):
        self.add_data_to_dict()
        print(self.stdList)
        while True:
            removeID = int(input("Remove StdID: "))
            self.stdList.pop(removeID)
            print("press 'yes' for another poll or press 'quit' anytime to exit:")
            anotherPoll = input()
            if anotherPoll == "quit":
                break
        print(self.stdList)


    def updateStd(self):
        self.add_data_to_dict()
        print(self.stdList)
        while True:
            updateID = int(input("Update StdID: "))
            updateColumn = input("Update Subject: ")
            updateValue = input("Update Result: ")
            stdlen = len(self.stdList)
            for i in range(stdlen):
                if (i == updateID):
                    self.stdList[updateID][updateColumn] = (updateValue)
                    break
            print("press 'yes' for another poll or press 'quit' anytime to exit:")
            anotherPoll = input()
            if anotherPoll == "quit":
                break
        print(self.stdList)

    def default(self):
        print("You Entered No is Invalid!!!")


obj = School()
#obj.updateStd()

userInput = int(input("Enter No: "))
func: dict = {
    1: obj.retrieve(),
    2: obj.removeStd(),
    3: obj.updateStd()
}

final = func.get(userInput, obj.default)
final()
    
