stdList=[]
dic={}

#
def add_data_to_dict():
    while True:
        stdID = input("StudentID: ")
        maths = input("Maths Result: ")
        science = input("Science Result: ")
        music = input("Music Result: ")
        english = input("English Result: ")
        social = input("Social Result: ")
        dic = {"StudentID ": stdID, "Maths ": maths, "Science ":science, "Music ":music, "English ":english, "Social ":social}
        stdList.append(dic)
        print("press 'yes' tfor another poll or press 'quit' anytime to exit:")
        anotherPoll = input()
        if anotherPoll == "quit":
            break



def retrieve():
    add_data_to_dict()
    print(stdList)

def removeStd():
    add_data_to_dict()
    print(stdList)
    while True:
        removeID = int(input("Remove StdID: "))
        stdList.pop(removeID)
        print("press 'yes' tfor another poll or press 'quit' anytime to exit:")
        anotherPoll = input()
        if anotherPoll == "quit":
            break
    print(stdList)


#retrieve()
removeStd()




