import os
import pickle
def Path(fileName):
    path =  os.path.join(os.getcwd(),fileName)
    return path
file=open(Path("Admin.txt"),"r")
file.close()
def getStuRoll(branch):
    file=open(Path("Student.txt"),"r")
    data=file.readlines()
    file.close()
    for i in data[::-1]:
        email=i.split("$")[1]
        if email[:-20]==branch:
            return int(email[-20:-11])+1
    else:
        match(branch):
            case "cse":
                return 240001001
            case "ee":
                return 240002001
            case "ce":
                return 240004001
            case "che":
                return 240008001
            case "mc":
                return 240041001
            case "mems":
                return 240005001
            case "me":
                return 240003001
            case "sse":
                return 240021001
    
def getString(message):
    a = input(message)
    if a.lower()=="exit":
        try:
            if file.closed:
                print("Forced Exit Performed")
                exit()
            else:
                file.close()
                print("Forced Exit Performed")
                exit()
        except Exception as e:
            #print(e)
            print("Forced Exit Performed")
            exit()
    else: 
        return a
def getInput(message):
    while True:
        a=input(message)
        if a.lower() == "exit":
            try:
                if file.closed:
                    print("Forced Exit Performed")
                    exit()
                else:
                    file.close()
                    print("Forced Exit Performed")
                    exit()
            except Exception as e:
                #print(e.with_traceback)
                print("Forced Exit Performed")
                exit()
        try:
            a= float(a)
            break
        except Exception:
            print("Invalid Input! Enter Again")
    return a
def Authentication(stu1adm0):
    if stu1adm0 == 0:
        file = open(Path("Admin.txt"),"r")
        #file = open(os.path.join(os.path.dirname('_file_'),"Data/Admin.txt"),"r")
    else: 
        #file = open(os.path.join(os.path.dirname('_file_'),"Data/Student.txt"),"r")
        file = open(Path("Student.txt"),"r")
    while True:
        username=getString("Enter Username: ")
        password=getString("Enter Password: ")
        # print(username)
        # print(password)
        #found = False
        row=[0]
        file.seek(0)
        while True:
            #print("Inside check")
            row = file.readline().split("$")
            if row==['']:
                #print("In end of file")
                print("Username or Password is valid! Enter Again")
                break
            #print(row)
            #print(username+" = "+row[1]+", "+password+" = "+row[2][:-1])
            if (username==row[1]) and (password==row[2][:-1]):
                print("Authentication Successful")
                print("Welcome",row[0])
                #found = True
                file.close()
                data=row ##Format: Name Branch Roll Marks
                if data[1][2]=="2":
                    branch=data[1][:2].upper()
                    roll=int(data[1][2:11])
                elif data[1][3]=="2":
                    branch=data[1][:3].upper()
                    roll=int(data[1][3:12])
                elif data[1][4]=="2":
                    branch=data[1][:4].upper()
                    roll=int(data[1][4:13])
                return roll

def NewUser():
    while True:
        print('''Select User Type:
1: Student
2: Admin''')
        type=getInput("Enter Choice: ")
        if type==1:
            print("Selected Student")
            name=getString("Enter Name: ")
            print('''Available Branch(s):
1: Computer Science and Engineering
2: Electrical Engineering
3: Mechanical Engineering
4: Mathematics and Computing
5: Civil Engineering
6: Chemical Engineering
7: Space Science and Engineering
8: Metallurgy and Material Science''')
            choice=getInput("Enter Choice: ")
            match(choice):
                case 1:
                    branch="cse"
                case 2:
                    branch="ee"
                case 3:
                    branch="me"
                case 4:
                    branch="mc"
                case 5:
                    branch="ce"
                case 6:
                    branch="che"
                case 7:
                    branch="sse"
                case 8:
                    branch="mems"
                case _:
                    print("Invalid Choice")
                    continue
            roll=getStuRoll(branch)
            file = open(Path("Student.txt"),"a")
            email=branch+str(roll)+"@iiti.ac.in"
            print("Your roll is:",roll)
            print("Your username is: "+email)
            # file.peek(0)
            # file.writeline(int(roll)+1)
            while True:
                password=getString("Enter a new Password: ")
                if password.find("$")==-1:
                    break
                else:
                    print("Password must not contain $")
            toWrite=name+"$"+email+"$"+password+"\n"
            file.seek(2)
            file.write(toWrite)
            # file.write()
            file.close()
            file=open(Path("Grades.bin"),"ab")
            pickle.dump([name,branch.upper(),roll,{}],file)
            file.close()
            print("User "+email+" Registered Successfully")
            return None
        if type==2:
            print("Selected Admin")
            name=getString("Enter Name: ")
            #branch=getString("Enter B")
            file = open(Path("Admin.txt"),"a+")
            file.seek(0)
            roll=file.readlines()[-1].split("$")[1][-20:-11]
            email="adm"+str(int(roll)+1)+"@iiti.ac.in"
            print("Your username is: "+email)
            #file.seek(0)
            #file.write(str(int(roll)+1)+"\n")
            #file.write("\n")
            while True:
                password=getString("Enter a new Password: ")
                if password.find("$")==-1:
                    break
                else:
                    print("Password must not contain $")
            file.seek(2)
            file.write(name+"$"+email+"$"+password+"\n")
            file.close()
            print("User "+email+" Registered Successfully")
            return None
        else: 
            print("Invalid Choice! Enter Again")

#Admin
def setCourse():
    file=open(Path("Course.txt"),"r+")
    file.seek(0)
    if file.read(1)=="Y":
        print("Courses Already Set")
        return None
    else:
        #pos=file.tell()
        file.seek(3,0)
        print("All Available Courses: ")
        courses=file.readlines(-1)
        sl=1
        #print(courses)
        for i in courses:
            print(str(sl)+": "+i[1:],end="")
            sl+=1
        #print()
        print("Enter 1 to Select the Course, else 0")
        sl=1
        i="a"
        file.seek(3,0)
        while True:
            #print(file.tell())
            i=file.readline()
            #print(i)
            if i=="":
                break
            setOrNot=getInput(str(sl)+": "+i[1:-1]+": ")
            sl+=1
            if setOrNot==1:
                pos=file.tell()+(-1)*(len(i))-1
                #print(pos)
                file.seek(pos,0)
                file.write("Y")
                pos=file.tell()+len(i[1:])+1
                file.seek(pos,0)
            elif setOrNot==0:
                pos=file.tell()+(-1)*(len(i[1:])+2)
                file.seek(pos,0)
                file.write("N")
                pos=file.tell()+len(i[1:])+1
                file.seek(pos,0)
            else:
                print("Invalid Choice! Enter Again")
                pos=file.tell()+(-1)*len(i)-1
                file.seek(pos,0)
                sl-=1
            
        file.seek(0)
        file.write("Y")
        file.close()
        print("Course Set Successfully")
        
def manageGrades():
    
    file=open(Path("Course.txt"),"r")
    course=file.readlines()
    file.close()
    while True:
        print('''Available Options:
1: Enter Grades 
2: Modify already entered Grades
3: Back
4: Exit''')
        choice=getInput("Enter Choice: ")
        if choice==3:
            return None
        if choice==4:
            exit()    
        file=open(Path("Grades.bin"),"rb")
        stuGrade=[]  #Format: Name Branch Roll Marks
        try:
            while True:
                stuGrade.append(pickle.load(file))
        except:
                file.close()
        if choice==1:
            left=0
            for i in stuGrade:
                if not i[3]:
                    left+=1
            print("Number of Students whose grades are left to be entered is:",left)
            for i in stuGrade:
                if i[3]:
                    continue
                print("Enter All Grades out of 10")
                print(i[0],i[1],i[2])
                sl=1
                for courseName in course[1:]:
                    if courseName[0]=="Y":
                        while True:
                            MARKS=getInput(str(sl)+": "+courseName[1:-1]+": ")
                            if MARKS>=0 and MARKS<=10:
                                break
                            else:
                                print("Grades must lie between 0 and 10")
                        i[3][courseName[1:-1]]=MARKS
                        sl+=1
                else:
                    file=open(Path("Grades.bin"),"wb")
                    for i in stuGrade:
                        pickle.dump(i,file)
                    file.close()
                    print("Grades of Roll",i[2],"entered successfully")
                left-=1
                if left==0:
                    print("Grades of all students entered successfully")
                    break
                enterFurther=getString("Want to enter the details of next Student(Left: "+str(left)+") (Y/anything else): ")
                if enterFurther.lower()=="y":
                    continue
                else:
                    break
            else:
                print("Grades of all students entered successfully")
        if choice==2:
            print("__Modifying Entered Grades__")
            roll=getInput("Enter Roll Number of the student: ")
            for i in stuGrade:
                if i[2]==roll:
                    if not i[3]:
                        print("Grades not entered yet")
                        if getString("Want to enter grades now (Y/anything else): ")!="Y":
                            break
                    print("Enter All Grades out of 10")
                    print(i[0],i[1],i[2])
                    sl=1
                    for courseName in course[1:]:
                        if courseName[0]=="Y":
                            while True:
                                MARKS=getInput(str(sl)+": "+courseName[1:-1]+"(Original: "+str(i[3][courseName[1:-1]])+"): ")
                                if MARKS>=0 and MARKS<=10:
                                    break
                                else:
                                    print("Grades must lie between 0 and 10")
                            i[3][courseName[1:-1]]=MARKS
                            #i[3][courseName[1:-1]]=MARKS
                            sl+=1
                    file=open(Path("Grades.bin"),"wb")
                    for j in stuGrade:
                        pickle.dump(j,file)
                    file.close()
                    print("Grades of Roll "+str(i[2])+" modified successfully")
                    break   
            else:
                print("No such roll found!")
                
#Student
def viewGrades(roll):
    file=open(Path("Grades.bin"),"rb")
      #Format: Name Branch Roll Marks
    found=False
    try:
        while True:
            student=pickle.load(file)
            if student[2]==roll:
                found=True
                break
    except:
            file.close()
    if not found:
        print("No such Roll exist!")
        return None
    if not student[3]:
        print("Grades not entered yet!")
        return None
    print("___Semester Performance Index___")
    print("Name:",student[0],"Roll:",student[2],"Branch:",student[1])
    print("Grades:")
    sum=0
    num=0
    for i in student[3]:
        print(i,": ",student[3][i],sep="")
        sum+=student[3][i]*4
        num+=4
    print("SPI:",sum/num)