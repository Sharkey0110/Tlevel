
#FUNCTIONS




#removed the repeating grade boundaries and appending from both original functions
def add():
    date = input("Enter date: ")
    tname = input("Enter your name: ")
    global sname
    sname = input("Enter studdents name: ")
    file = open(sname + ".txt","w")
    file.write("Written on " +date + "\nWritten by " + tname + "\nStudent name: " + sname)
    file.close()
    gradeinfo()
    
    

def app():
    global sname
    sname = input("Enter name of file you wish to append (Students name): ")
    date = input("Enter date: ")
    tname = input("Enter your name: ")
    file = open(sname + ".txt","w")
    file.write("Changed on " +date + "\nChanged by " + tname + "\nStudent name: " + sname)
    file.close()
    file = open(sname + ".txt","a")
    gradeinfo()
    
#Added another function to calculate and addd grades to text file using global variables
    
def gradeinfo():
    file = open(sname + ".txt","a")
    amount = int(input("How mnay tests did student complete: "))
    for x in range (amount):
        test = input("Enter test completed: ")
        tscore = int(input("Enter score of test completed: "))
        if tscore >= 80:
            grade = "A*"
        elif tscore < 80 and tscore >= 70:
            grade = "A"
        elif tscore <70 and tscore >=60:
            grade = "B"
        elif tscore <60 and tscore >=50:
            grade = "C"
        elif tscore <50 and tscore >=40:
            grade = "D"
        else:
            grade = "Fail"
        file.write("\nType of test: " + test + "\nScore: " + str(tscore) + "\ngrade: " + grade)
    file.close()

def readfl():
    sname = input("Whos file would you like to read: ")
    file = open(sname + ".txt","r")
    print(file.read() + "\n")
    file.close()

#MAIN
while True:
    Choice = int(input("\n1)Add file\n2)Append existing file\n3)read file\n4)Exit Menu\nEnter number: "))
    if Choice == 1:
        add()
    elif Choice == 2:
        app()
    elif Choice == 3:
        readfl()
    else:
        break
        
       
        
