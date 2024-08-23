from Python.Common import getInput
from Python.Common import Authentication

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

    elif choice == 2:
        print("**Student Panel**")
        Authentication(1)
    elif choice == 3:
        print("**New User Registration**")
        pass
    elif choice == 4:
        exit()
    else:
        print("Invalid Choice, Enter Again!")