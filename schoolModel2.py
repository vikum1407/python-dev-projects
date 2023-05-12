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
        dic = {"StudentID": stdID, "Maths": maths, "Science":science, "Music":music, "English":english, "Social":social}
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
        print("press 'yes' for another poll or press 'quit' anytime to exit:")
        anotherPoll = input()
        if anotherPoll == "quit":
            break
    print(stdList)

def updateStd():
    add_data_to_dict()
    print(stdList)
    while True:
        updateID = int(input("Update StdID: "))
        updateColumn = input("Update Subject: ")
        updateValue = input("Update Result: ")
        stdlen = len(stdList)
        for i in range(stdlen):
            if(i==updateID):
                stdList[updateID][updateColumn]=(updateValue)
                break
        print("press 'yes' for another poll or press 'quit' anytime to exit:")
        anotherPoll = input()
        if anotherPoll == "quit":
            break
    print(stdList)

def default():
    print("You Entered No is Invalid!!!")


userInput = int(input("Enter No: "))

# if userInput == 1:
#     retrieve()
# elif userInput == 2:
#     removeStd()
# else:
#     default()

func: dict = {
    1: retrieve,
    2: removeStd,
    3: updateStd
}

final = func.get(userInput, default)
final()
