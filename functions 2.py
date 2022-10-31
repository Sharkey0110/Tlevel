import random


def name(firstname,age):
    return("Your name is " + firstname + " and you are " + str(age) + " Years old")



def add(num1,num2):
    return ("The answer is " + str(num1+num2))

def rannum():
    return("Your numbers are " + str(random.randint(1,100)) + " and " + str(random.randint(1,100)))
  

def bignum(num1,num2,num3):
    if num1 > num2 and num1 > num3: print(str(num1) + " is the biggest number")
        
        
    if num2 > num1 and num2 > num3: print(str(num2) + " is the biggest number")
        
        
    if num3 > num2 and num3 > num1: print(str(num3) + " is the biggest number")
        


    
def fizzbizz():
    for x in range(50):
        if (x % 3 == 0) and (x % 5 == 0):
            print("FizzBuzz")
        elif(x % 3 == 0):
            print("Fizz")
        elif(x % 5 == 0):
            print("Buzz")
        else:
            print(x)

def time(min):
    return ("That is equal to " + str(min * 60) + " seconds")




def dayage(age):
    return ("That is equal to " + str(age*365) + " days")

def capin(word):
    List = []
    for x in range (len(word)):
        if word[x] == word.upper()[x]:
            List.append(x)
    print(List)




def mid(word):
    if len(word)% 2 == 0:
        print(" ")
    else:
        print(word[(len(word))//2])
            
         
     
     
    



    

while True:
    choice = int(input("\nNumber: "))
    if choice == 1:
        fizzbizz()
        
    elif choice == 2:
        (bignum(int(input("Enter number1: ")),int(input("Enter number2: ")),int(input("Enter number3: "))))
        
    elif choice == 3:
        print(rannum())
        
    elif choice == 4:
        print(add(int(input("Enter first number 1: ")),int(input("Enter number 2: "))))
        
    elif choice == 5:
        print(name(input("Enter name: "),int(input("Enter age: "))))
        
    elif choice == 6:
        print(time(int(input("Enter time in minutes: "))))
      
    elif choice == 7:
           print(dayage(int(input("Enter your age: "))))

    elif choice == 8:
        (capin(input("Enter word: ")))
    elif choice == 9:
         mid(str(input("Enter word: ")))



               
    else:
        print("ERROR\n")



