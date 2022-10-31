

def search(target):
        if target in numlist2:
            print("Number found")
        else:
            print("Number not found")



def bignum():
    biggest = numlist2[0]
    for x in numlist2:
        if biggest < x:
            biggest = x
    return biggest
            
        
def totalsum():
    total = 0
    for x in range (len(numlist2)):
        total +=numlist2[x]
    return total

def smallnum():
    smallest = numlist2[0]
    for x in numlist2:
        if smallest > x:
            smallest = x
    return smallest


def totalproduct():
     total = 1
     for x in range (len(numlist2)):
        total *= numlist2[x]
     return total


def therange():
    biggest = numlist2[0]
    for x in numlist2:
        if biggest < x:
            biggest = x

    smallest = numlist2[0]
    for y in numlist2:
         if smallest > y:
             smallest = y

    return(biggest-smallest)


def average():
        total = 0
        for x in range (len(numlist2)):
                total += numlist2[x]
        return(total/setamount)


def medium():
        numlist2.sort()
        return numlist2[setamount//2]

    
    
numlist2 = []
setamount = int(input("How long will the list be: "))
for x in range (setamount):
    num = int(input("Enter number: "))
    numlist2.append(num)



    


    
iput = int(input("1) Search\n2) Smallest number\n3) Biggest number\n4) Total sum\n5) Total product\n6) Range\n7) Average\nEnter number: "))
if iput == 1:
        (search(int(input("Enter number to search: "))))
elif iput == 2:
        print(smallnum())
elif iput == 3:
        print(bignum())
elif iput == 4:
        print(totalsum())
elif iput == 5:
        print(totalproduct())
elif iput == 6:
        print(therange())
elif iput == 7:
        print(average())
elif iput == 8:
        print(medium())
else:
        print("invailid")
        
        
        
        
        
