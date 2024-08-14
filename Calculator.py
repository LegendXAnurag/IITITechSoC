print("Welcome to Calculator")
#e = 2.7182818284590
pi = 3.1415926535897
def getInput(message):
    while True:
        a=input(message)
        try:
            a= float(a)
            break
        except Exception:
            print("Invalid Input! Enter Again")
    return a
def getAngle():
    while True:
        radOrDeg = input("Want to give Radians or Degrees (rad/deg)? ")
        if radOrDeg in ["rad","deg"]:
            if radOrDeg == "rad":
                return getInput("Enter Radians: ")
            else:
                angle= getInput("Enter Degrees: ")
                if (angle)%360==0:
                    return "0FORM"
                elif (angle-90)%360==0:
                    return "90FORM"
                elif (angle-180)%360==0:
                    return "180FORM"
                elif (angle-270)%360==0:
                    return "270FORM"
                else:
                    return angle*pi/180
        else: 
            print("Invalid Input! Enter Again")

def getOperands():
    a=getInput("Enter Operator1: ")
    b=getInput("Enter Operator2: ")
    return (a,b)
def factorial(n):
    value=1
    if n==0:
        return 1
    if n==1:
        return 1
    for i in range(1,n+1):
        value*=i
    return value
def sin(rad):
    if rad == "0FORM":
        return 0
    if rad == "90FORM":
        return 1
    if rad == "180FORM":
        return 0
    if rad == "270FORM":
        return -1
    value=0
    sign=0
    for i in range(1,100,2):
        value+= ((-1)**sign)*(rad**i)/factorial(i)
        sign+=1
    return value
def cos(rad):
    if rad == "0FORM":
        return 1
    if rad == "90FORM":
        return 0
    if rad == "180FORM":
        return -1
    if rad == "270FORM":
        return 0
    value=0
    sign=0
    for i in range(0,100,2):
        value+= ((-1)**sign)*(rad**i)/factorial(i)
        sign+=1
    return value
def tan(rad):
    if rad == "0FORM":
        return 0
    if rad == "90FORM":
        return "Not Defined ((+/-)Infinity)"
    if rad == "180FORM":
        return 0
    if rad == "270FORM":
        return "Not Defined ((+/-)Infinity)"
    return sin(rad)/cos(rad)
#def cosec(rad):
#    return 1/sin(rad)
#def sec(rad):
#    return 1/cos(rad)
#def cot(rad):
#    return cos(rad)/sin(rad)
def ln(argument):
    n=10000
    return n*((argument**(1/n))-1)


while True:
    print('''Available commands:-
1: Add
2: Subtract
3: Multiply
4: Divide
5: Exponent
6: Trigonometry
7: Logarithms
8: Quadratic Solver
9: Exit''')
    
    choice = getInput("Select Command(Enter number): ")

    if choice == 1:
        print("Performing Addition")
        operands = getOperands()
        print("Result: ",operands[0]+operands[1])
    elif choice == 2:
        print("Performing Subtraction")
        operands = getOperands()
        print("Result: ",operands[0]-operands[1])
    elif choice == 3:
        print("Performing Multiplication")
        operands = getOperands()
        print("Result: ",operands[0]*operands[1])
    elif choice == 4:
        print("Performing Division")
        operands = getOperands()
        if operands[1]==0:
            print("Cannot Divide by Zero")
            print("Moving Back to Main Menu")
            continue
        print("Result: ",operands[0]/operands[1])

    elif choice ==5: 
        print("Performing Exponent")
        while True:
            try:
                base = float(input("Enter base: "))
                raisedTo = float(input("Enter power to raise upto: "))
                print("Result: ",base**raisedTo)
                break
            except Exception:
                print("Invalid data type enter integer or float only.")

    elif choice ==6:
        while True:
            print('''Available Trigonometry function:
1: Sin
2: Cos
3: Tan
4: Back''')
#4: Cosec
#5: Sec
#6: Cot''')
            choice = getInput("Select Command(Enter number): ")
            if choice==1:
                print("Performing Sine")
                print("Result: ",sin(getAngle()))
            elif choice==2:
                print("Performing Cosine")
                print("Result: ",cos(getAngle()))
            elif choice==3:
                print("Performing Tangent")
                print("Result: ",tan(getAngle()))
            elif choice==4:
                break
            else:
                print("Choice invalid! Enter Again")
        #if choice==4:
        #    print("Performing Cosecant")
        #    print("Result: ",cosec(getInput("Enter Radians: ")))
        #if choice==5:
        #    print("Performing Secant")
        #    print("Result: ",sec(getInput("Enter Radians: ")))
        #if choice==6:
        #    print("Performing Cotangent")
        #    print("Result: ",cot(getInput("Enter Radians: ")))

    elif choice == 7:
        print("Performing Logarithm")
        while True:
            baseChoice = input("Use Natural Base(y/n): ")
            if baseChoice in ["y","n"]:
                break
            print("Invalid input, enter (y/n) only!")
        #baseChoice = getInput("Use Natural Base(y/n): ","y")
        if baseChoice=="y":
            base = 2.7182818284590
        elif baseChoice=="n":
            while True: 
                base = getInput("Enter Base: ")
                if base<0:
                    print("Enter Valid Base(>0,!=1)")
                    continue
                elif base==1:
                    print("Enter Valid Base(>0,!=1)")
                    continue
                break
        while True:
            argument = getInput("Enter Argument: ")
            if argument<0:
                print("Enter Valid Argument(>0)")
                continue
            break
        if base==2.7182818284590:
            print("Result: ",ln(argument))
        else:
            print("Result: ",ln(argument)/ln(base))

    elif choice == 8:
        print("Performing Quadratic Solver")
        print("For Quadratic Equation ax^2 + bx + c=0, Enter the coefficients of the quadratic equations:")
        while True:
            a = getInput("a: ")
            if a==0:
                print("a cannot be zero! Enter Again")
                continue
            break
        b = getInput("b: ")
        c = getInput("c: ")
        D= b**2-4*a*c
        if D<0:
            print("Roots are imaginary")
            D*=-1
            print("Roots: ",-b/(2*a),"+",(D**0.5)/(2*a),"i, ",-b/(2*a),"-",(D**0.5)/(2*a),"i",sep="")
            continue
        if D==0:
            print("Roots are real and equal\nRoot: ",-b/2*a,sep="")
            continue
        if D>0: 
            print("Roots of the Quadratic are Real and Distinct\nRoots: ",(-b+(D**0.5))/(2*a),", ", (-b-(D**0.5))/(2*a),sep="")

    elif choice == 9:
        exit()
    else:
        print("Invalid Choice, Enter Again!")