from Controllers.subjectController import crudSubject
from Controllers.studentController import crudStudent
from Controllers.resultController import crudResult


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
    choice = input("Enter Your Choice: ")
    match choice:
        case "A":
            crudStudent().controller()
        case "B":
            crudSubject().controller()
        case "C":
            crudResult().controller()
        case "Q":
            break

