def primcheck(number):
    for x in range(2,number):
        if (number%x ==0):
            return False
        return True

#print(primcheck(int(input("Enter number: "))))



def calc(num1,num2):
    choice = int(input("1)Add\n2)subtract\n3)multiply\n4)Divide\nEnter number: "))
    if choice == 1:
        return num1 + num2
    elif choice == 2:
        return num1 - num2
    elif choice == 3:
        return num1*num2
    else:
        try:
            return num1/num2
        except ZeroDivisionError:
            return 0

    
while True:
    print(calc(int(input("Enter number 1: ")),int(input("Enter number 2: "))))
    
