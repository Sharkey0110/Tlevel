
#Shout out max/markus
import random
import json

#FUNCTION



datastock = {
    }

def load():
    global datastock
    file = open("Stock.txt","r")
    read = file.read()

    if read == "":
        datastock = {}
    else:
        js = read.replace("'", '"')
        datastock = json.loads(js)


def additem(dataset,name,dep,pid,location,price,stock):
    datastock[name]= {}
    datastock[name]["Department"] = dep
    datastock[name]["ProductID"] = pid
    datastock[name]["Location"] = location
    datastock[name]["Price"] = price
    datastock[name]["Price with Vat"] = round((price * 1.2),2)
    datastock[name]["Quantity"] = stock
    file = open("Stock.txt","w")
    file.write(str(datastock))
    file.close()


    
 
    
def stockadd(name,change):
    value = input("Change value here: ")
    t = type(datastock[name][change])

    if t == int:
        value = int(value)
    elif t == float:
        value = float(value)

    datastock[name][change] = value
    file = open("Stock.txt","w")
    file.write(str(datastock))
    file.close
    

def look(descision):
    if descision == 1:
            
            find = input("\nEnter product name: ")
            print(datastock[find],"\n")
            if input("Would you like to buy this item y/n: ") == "y":
                datastock[find]["Quantity"] -= 1
                file = open("Stock.txt","w")
                file.write(str(datastock))
                file.close

                
                
    elif descision == 2:
        find = input("\nEnter product department: ")

                    

                    
    else:
        find = input("\nEnter product ID ")
    
     
     
    

#MAIN
load()

print("You can only search by item name currently and items are not automatically given an ID but everything else works besides that\n")
while True:

    
    choice = int(input("\n1)Search for products\n2)Add products\n3)Edit existing product\n4)Print all of database\n5)Exit\nEnter number: "))
    if choice == 1:
        look(int(input("\n1)Search by name\n2)Search by Department\n3)Search by ID\nEnter number: ")))
      
        
                 
    elif choice == 2:
        
             
        (additem(datastock,input("\nEnter name "),input("Enter department "),int(input("Enter ID ")),input("Enter location "),float(input("Enter Price ")),int(input("Enter stock "))))
        

    elif choice == 3:
        print(stockadd(input("\nEnter product to append: "),input("Enter what key to edit: ")))
    
 
    elif choice == 4:
        #Print all
        file = open("Stock.txt","r")
        print("\n" + file.read())
        file.close()
        
    
    else:
        break
exit()
    
