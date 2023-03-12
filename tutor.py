#IMPORT

import json
import random


#FUNCTIONS

tutorpop = {
    }


def load():
    global tutorpop
    file = open ("formgroup.txt","r")
    read = file.read()

    if read == "":
        tutorpop = {}
        
    else:
        js = read.replace("'", '"')
        tutorpop = json.loads(js)



    

def login():



    uname = "JackLeeman"
    pword = "password"
    print("type exit on username to exit")
    username = input("Enter username: ")
    password = input("Enter password: ")
    if username == uname and password == pword:
        print("Welcome, Mr Leeman.\n")
        menu()
    elif username ==  "exit":
        exit()
    else:
        print("Invalid\n")
        login()
        

def readfl():
    choice = input("\n1)Read data file\n2)Read student report\n3)Go back\nEnter choice: ")
    if choice == "1":
        print(tutorpop)
        readfl()
    elif choice == "2":
        find = input("\nEnter name of student: ")
        try:
            file = open(find + " report.txt","r")
            print("\n" +file.read())
            file.close()
            readfl()
        except:
            print("File couldnt be found")
            readfl()
    elif choice == "3":
        menu()
    else:
        print("\nInvalid choice")
        readfl()
    


def menu():
    choice = input("1)Add info\n2)Search students\Make report\n3)Read files\n4)Log out\nEnter choice: ")
    if choice == "1":
        add(input("enter student first name: "),input("enter student last name: "),input("Enter student day born: "),input("Enter student month born: "),input("Enter student year born: "),input("Enter student address: "),input("Enter students phone number: "),input("Enter students gender: "))
    

    elif choice == "2":
        search()
    

    elif choice == "3":
        readfl()

        
    elif choice == "4":
        print("Goodbye, Mr Leeman.\n")
        login()
        

    else:
        print("\nInvalid")
        menu()



def add(fname,lname,day,month,year,address,phone,gender):
    
    while not (gender.lower() == "male" or gender.lower() == "female"):
        gender = input("Enter male or female: ")
    while fname.isalpha() == False:
        fname = input("Enter valid first name: ")
    while lname.isalpha() == False:
        lname = input("Enter valid last name: ")
    while day.isnumeric() == False or len(day) < 2:
        day = input("Enter valid day: ")
    while month.isnumeric() == False or len(month) < 2:
        month = input("Enter valid month: ")
    while year.isnumeric() == False or len(year) < 4:
        year = input("Enter valid day: ")
    while len(phone) < 10 or phone.isnumeric() == False:
        phone = input("Enter valid phone number: ")
        

    studentID = random.randint(1000000,9999999)
    studentID = str(studentID)
    print("\nThe assinged student id is",studentID) 
    tutorpop[studentID] = {}
    tutorpop[studentID]["fname"] = fname
    tutorpop[studentID]["lname"] = lname
    tutorpop[studentID]["dob"] = (day + "/" + month + "/" + year)
    tutorpop[studentID]["address"] = address
    tutorpop[studentID]["phone"] = "+44 " + phone[0:4] + " " + phone[4:9]
    tutorpop[studentID]["gender"] = gender
    tutorpop[studentID]["Tutor"] = "11H"
    tutorpop[studentID]["Schoolemail"] = (fname + lname +".school.com")
    file = open("formgroup.txt","w")
    file.write(str(tutorpop))
    file.close()
    menu()


def search():
    find = input("\nEnter stuents id (input exit to exit): ")
    if find == "exit":
        menu()
    try:
        print(tutorpop[find])
        if input("\nWould you like to write a report on this student? (y/n): ") == "y":
            file = open(tutorpop[find]["fname"] + " " + tutorpop[find]["lname"] + " report.txt","w")
            file.write(tutorpop[find]["fname"] + " " + tutorpop[find]["lname"] + "   " + tutorpop[find]["gender"] + "\n" + tutorpop[find]["dob"] + "   " + tutorpop[find]["address"] + "   " + tutorpop[find]["phone"] + "\n")
            report = input("\nAdd report notes: ")
            file.write("\n" + report)
            if input("\nEnter test results of the student (y/n): ") == "y":
                amount = int(input("\nHow mnay tests did student complete: "))
                for x in range (amount):
                    test = input("\nEnter test completed: ")
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
                    file.write("\nType of test: " + test + "\nScore: " + str(tscore) + "\ngrade: " + grade + "\n")   
            file.close()
            print("\nreport added")
            menu()
    except:
        print("ID not found")
        search()
    else:
        menu()
                 


#MAIN

load()
login()
