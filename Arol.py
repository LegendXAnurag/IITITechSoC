from Function import getInput
from Function import Authentication
from Function import NewUser
from Function import setCourse
from Function import manageGrades
from Function import viewGrades

print("Welcome to AROL")
while True:
    print('''1: Admin (Existing)
2: Student (Existing)
3: New User Registration 
4: Exit''')
    choice = getInput("Select Command(Enter Number): ")
    if choice == 1:
        print("**Admin Panel**")
        Authentication(0)
        while True:
            print('''Available Options:
1: Select the courses for this Semester
2: Manage Grades of Students
3: View Grade Sheet of Students
4: Back
5: Exit''')
            choice=getInput("Enter Choice: ")
            match(choice):
                case 1:
                    setCourse()
                case 2:
                    pass
                    manageGrades()
                case 4:
                    break
                case 5:
                    exit()
                case 3:
                    roll=getInput("Enter the roll of student: ")
                    viewGrades(roll)
                case _:
                    print("Invalid Choice! Enter Again")

    elif choice == 2:
        print("**Student Panel**")
        roll=Authentication(1)
        while True:
            print('''Available Options:
1: View Grade Sheet
2: Back
3: Exit''')
            choice=getInput("Enter Choice: ")
            match(choice):
                case 1:
                    pass
                    viewGrades(roll)
                case 2:
                  break
                case 3:
                    exit()
    elif choice == 3:
        print("**New User Registration**")
        NewUser()
    elif choice == 4:
        exit()
    else:
        print("Invalid Choice, Enter Again!")