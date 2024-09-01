from Function import getInput
from Function import Path
import pickle
print('''Options:
1: Reset all data
2: Reset course set status and student marks
3: Set Sample Data(Student & Teachers IDs, Course Set, Grades of some students)''')
choice=getInput("Enter Choice: ")
if choice==1:
    file=open(Path("Course.txt"),"r+")
    file.seek(0)
    file.write("N")
    file.close()
    file=open(Path("Student.txt"),"w")
    file.close()
    file=open(Path("Admin.txt"),"w")
    file.close()
    file=open(Path("Grades.bin"),"wb")
    file.close()
    print("Reset successfull")
if choice==2:
    file=open(Path("Course.txt"),"r+")
    file.seek(0)
    file.write("N")
    file.close()
    file=open(Path("Grades.bin"),"rb")
    stuData=[]
    while True:
        try:
            stuData.append(pickle.load(file)[:2])
        except:
            file.close()
            break
    file=open(Path("Grades.bin"),"wb")
    for i in stuData:
        pickle.dump(i,file)
    file.close()
    
    
    print("Reset of Course set status and student marks successful")
if choice==3:
    file=open(Path("Student.txt"),"w")
    file.write('''Abhishek Verma$cse240001001@iiti.ac.in$abc
Alaya Vella d'Cruz$cse240001002@iiti.ac.in$abc
Ankur Singh$cse240001003@iiti.ac.in$abc
Anurag Prasad$cse240001004@iiti.ac.in$abc
Arnav Kumar$ee240002001@iiti.ac.in$abc
Aryaman Tiwari$cse240001005@iiti.ac.in$abc
Ayush Singh Rana$cse240001006@iiti.ac.in$abc
Bhupesh Singh$cse240001007@iiti.ac.in$abc
Siddha Nema$ee240002002@iiti.ac.in$abc
''')
    file.close()
    file=open(Path("Admin.txt"),"w")
    file.write('''Nagendra Kumar$adm240009001@iiti.ac.in$abc
Abhishek Srivastava$adm240009002@iiti.ac.in$abc
Aman Khurana$adm240009003@iiti.ac.in$abc
Aratrika Das$adm240009004@iiti.ac.in$abc
''')
    file.close()
    file=open(Path("Course.txt"),"w")
    file.write('''Y
YLanguage and Composition HS109
YCalculus-1 & 2 MA101N/103
YBasics of Physics PH107
YPhysics Lab PH157
YEngineering Mechanics ME101
YBasic Electrical Engieering EE101
NChemistry CH105
NChemistry Lab CH155
YMakerSpace IC151
YComputer Programming CS103
YComputer Programming Lab IC152
YHistory of Tribal and Folk Art HS121
NCultural Sociology HS123
''')
    file.close()
    file=open(Path("Grades.bin"),"wb")
    #Format: Name Branch Roll Grades
    pickle.dump(["Abhishek Verma","CSE",240001001,{"Language and Composition HS109":8,"Calculus-1 & 2 MA101N/103":8,"Basics of Physics PH107":8,"Physics Lab PH157":8,"Engineering Mechanics ME101":9,"Basic Electrical Engieering EE101":9,"MakerSpace IC151":9,"Computer Programming CS103":6,"Computer Programming Lab IC152":7,"History of Tribal and Folk Art HS121":7}],file)
    pickle.dump(["Alaya Vella d'Cruz","CSE",240001002,{"Language and Composition HS109":8,"Calculus-1 & 2 MA101N/103":8,"Basics of Physics PH107":7,"Physics Lab PH157":8,"Engineering Mechanics ME101":9,"Basic Electrical Engieering EE101":9,"MakerSpace IC151":9,"Computer Programming CS103":6,"Computer Programming Lab IC152":7,"History of Tribal and Folk Art HS121":9}],file)
    pickle.dump(["Ankur Singh","CSE",240001003,{}],file)
    pickle.dump(["Anurag Prasad","CSE",240001004,{"Language and Composition HS109":10,"Calculus-1 & 2 MA101N/103":10,"Basics of Physics PH107":10,"Physics Lab PH157":10,"Engineering Mechanics ME101":10,"Basic Electrical Engieering EE101":10,"MakerSpace IC151":10,"Computer Programming CS103":6,"Computer Programming Lab IC152":10,"History of Tribal and Folk Art HS121":9}],file)
    pickle.dump(["Arnav Kumar","EE",240001001,{"Language and Composition HS109":9,"Calculus-1 & 2 MA101N/103":8,"Basics of Physics PH107":8,"Physics Lab PH157":8,"Engineering Mechanics ME101":9,"Basic Electrical Engieering EE101":9,"MakerSpace IC151":9,"Computer Programming CS103":6,"Computer Programming Lab IC152":7,"History of Tribal and Folk Art HS121":10}],file)
    pickle.dump(["Aryaman Tiwari","CSE",240001005,{}],file)
    pickle.dump(["Ayush Singh Rana","CSE",240001006,{}],file)
    pickle.dump(["Bhupesh Soni","CSE",240001007,{"Language and Composition HS109":8,"Calculus-1 & 2 MA101N/103":6,"Basics of Physics PH107":6,"Physics Lab PH157":7,"Engineering Mechanics ME101":9,"Basic Electrical Engieering EE101":6,"MakerSpace IC151":8,"Computer Programming CS103":6,"Computer Programming Lab IC152":7,"History of Tribal and Folk Art HS121":7}],file)
    pickle.dump(["Siddha Nema","EE",240001002,{}],file)
    file.close()
    print("Sample Data Set Successfully")