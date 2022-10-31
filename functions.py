#IMPORTS


#FUNCTIONS
def time():
    min = int(input("Enter amount of minutes: "))
    secs = min * 60
    print("That is equal to " + str(secs) + " seconds")

def add():
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    ans = num1 + num2
    print("The answer is " +str(ans))


def age():
    year = int(input("Enter age: "))
    days = year * 365
    print("That is equal to " + str(days) + " days")
    



#MAIN
for x in range(3):
    time()
    add()
    age()
