import random
def getString(message):
    a = input(message)
    if a.lower()=="exit":
        exit()
    else: 
        return a
def getInput(message):
    while True:
        a=input(message)
        if a.lower() == "exit":
            if file.closed():
                exit()
            else: 
                file.close()
                exit()
        try:
            a= float(a)
            break
        except Exception:
            print("Invalid Input! Enter Again")
    return a
def Authentication(stu1adm0):
    if stu1adm0 == 0:
        file = open("./Data/Admin.txt","r")
    else: 
        file = open("./Data/Student.txt","r")
    while True:
        username=getString("Enter Username: ")
        password=getString("Enter Password: ")
        row=[0]
        #found = False
        while (not row):
            row = file.readline().split("$")
            if (username==row[1]) and (password==row[2]):
                print("Authentication Successful")
                print("Welcome ",row[0])
                #found = True
                file.close()
                return row
        print("Username or Password is valid! Enter Again")

def NewUser():
    while True:
        type = getInput('''Select User Type:
1: Student
2: Admin''')
        if type==1:
            print("Selected Student")
            name=getString("Enter Name")
            branch=getString('''Enter Branch:
1: Computer Science and Engineering
2: Electrical Engineering
3: Mechanical Engineering
4: Mathematics and Computing
5: Civil Engineering
6: Chemical Engineering
7: Space Science and Engineering
8: Metallurgy and Material Science''')

            file = open("./Data/Student.txt","r")
        if type==2:
            print("Selected Admin")
            name=getString("Enter Name")
            file = open("./Data/Admin.txt","r")
        else: 
            print("Invalid Choice! Enter Again")
