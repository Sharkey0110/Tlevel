#IMPORTS
#Inputs the dictionary as a variable
with open ("Updatedstock.txt","r") as file:
    datastock = eval(file.read())

#allows the user to select words using numbers rather than requiring them to type the words out later in the code
search_names = ["Name","Department","ID"]


#FUNCTIONS

#saves the new inputs to the text file to allow the user to exit the program at any point and not lose progress
def save(datastock):
    with open("UpdatedStock.txt","w") as file:
        file.write(str(datastock))


#Lets the user search for products by ID, name or Department
def search(choice,find,datastock):
    #If the user searches by ID, the program searches the full dictionary rather than the embedded dictionaries 
    if choice == "ID":
        try:
            return (datastock[find])
        
        except:
            return "Product not found"
    #If the user searches by name or department, the program searches each embedded dictionary
    else:
        products = []
        for x in datastock:
            if datastock[x][choice] == find:
                products.append(datastock[x])
        return products
            
        return "Product not found"

    

#The code that appends the added product to the text file and dictionary
def add_product(name,department,location,price,amount,datastock):
    #Creates the unique ID by counting how many products are in the system and filling the empty space with 0s to create a 7 digit code
    ID = 1
    for x in datastock:
        ID += 1
    ID = str(ID).zfill(7)

    datastock[ID] = {}    
    datastock[ID]["Name"] = name
    datastock[ID]["Department"] = department
    datastock[ID]["Location"] = location
    datastock[ID]["Price"] = price
    datastock[ID]["Amount"] = amount
    save(datastock)
    
    
#Appends the value attached to a specific key on a specific product
def edit_product(ID,key,value,datastock):
    datastock[ID][key] = value
    save(datastock)



#MAIN

#Infinite menu code in a while loop which only breaks if the exit option is selected
while True:
    try:
        menu = int(input("\n1)Search for products\n2)Add products\n3)Edit existing products\n4)Print full database\n5)Exit\nEnter choice: "))

        #The code that asks users for inputs to search for a product
        if menu == 1:
            while True:
                try:
                    choice = int(input("\n1)Search by name\n2)Search by department\n3)Search by ID\n4)Exit\nEnter choice: "))

                    #Lets user select department, ID or name without needing them to type out the words using the list in the imports section
                    if choice == 1 or choice == 2 or choice == 3:
                        find = input("Enter product " +search_names[choice-1] + " : ")
                        choice = search_names[choice-1]
                        product = search(choice,find,datastock)
                        print(product)

                    elif choice == 4:
                        break
                        
                    else:
                        print("\nPlease select number in range")
                except:
                    print("\nPlease select number")
                    

        #Code that takes in inputs for products and validates them to ensure answers are reasonable
        elif menu == 2:
            product_name = input("\nEnter name of product: ")
            while len(product_name) == 0 or product_name.isspace == True:
                product_name = input("\nEnter name of product: ")

            department = input("\nEnter department of product: ")
            while len(department) == 0 or department.isspace == True:
                department = input("\nEnter department of product: ")

            location = input("\nEnter location of warehouse storing product: ")
            while len(location) == 0 or department.isspace == True:
                location = input("Enter location ofwarehouse storing product: ")

            while True:
                try:
                    price = float(input("\nEnter price of product: £"))
                    round(price,2)
                    break
                except:
                    print("\nPlease enter valid price")

            while True:
                try:
                    amount = int(input("\nEnter amount of stock: "))
                    break
                except:
                    print("\nPlease enter valid amount")
                    
            add_product(product_name,department,location,price,amount,datastock)
            print("Product added")
            

            
        #the code that takes in inputs to locate the correct product to edit, and what value will be changed
        elif menu == 3:
            while True:
                ID = input("\nEnter Product ID (1 to exit): ")
                if ID == "1":
                    break
                else:
                    try:
                        print(datastock[ID])
                        if input("\nIs this the product you wish to edit(Y/N): ").upper() == "Y":
                            key_change = input("\nWhich value do you wish to change: ")
                            
                            while key_change not in datastock[ID].keys():
                                key_change = input("\nWhich value do you wish to change: ")
                    
                            if key_change == "Price":
                                while True:
                                    try:
                                        value_change = float(input("Enter new price: £"))
                                        value_change = value_change.round(2)
                                        break
                                    except:
                                        print("Enter valid price")
                                    

                            elif key_change == "Amount":
                                while True:
                                    try:
                                        value_change = int(input("Enter new amount: "))
                                        break
                                    except:
                                        print("Enter valid amount")

                            else:
                                value_change = input("Enter new " + key_change + " :")
                                while len(value_change) == 0 or value_change.isspace == True:
                                    value_change = input("Enter new",key_change,":")

                            edit_product(ID,key_change,value_change,datastock)
                    except:
                        print("Product not found")


        elif menu == 4:
            print(datastock)
                            
        elif menu == 5:
            exit()
            
        else:
            print("\nMenu option out of range")
            
    except:
        print("\nInvalid menu option")
                                
                                        
                        
            
            
            
                    
                
                
            


                    
                    
            
            
