Functions

def fileupdate():
    #Reloads the file so the new data can be read, allows program to do several actions without needing
    #to be reloaded manually
    with open("carfile.txt","w") as file:
        file.write(str(report))
    print("File updated")



def add():
    #Searches for the plate inputted in the datafile
    doNext = True
    plate = input("\nEnter plate: ")
    while len(plate) < 5 or plate.isspace() == True:
        plate = input("Enter plate: ")
    for x in report:
        if x == plate:
            #If plate can be found
            print("\nLicense plate found")
            #Counts how many fines that plate has and names the new dictionary the next number to avoid overwriting
            count = 1
            for y in report[plate]["Fines"]:
                count += 1
            count = str(count)


            #details are inputted and tested to make sure logical answers are given
            test = True
            while test:
                speedlim = input("Enter speed limit: ")
                if speedlim.isnumeric() == True:
                    if int(speedlim) < 160:
                        test = False

            speed = input("Enter speed: ")
            while speed.isnumeric() == False: speed = input("Enter speed: ")
            if int(speed) <= int(speedlim):
                print("Car was not speeding")
                doNext = False
                continue
            fine = input("Enter fine: £")
            while fine.isnumeric == False: fine = int(input("Enter fine: "))
            fine = ("£" + fine)

            #The new report is appended into the dictionary and saved to a file
            report[x]["Fines"][count] = {}
            report[x]["Fines"][count]["Speed limit"] = speedlim
            report[x]["Fines"][count]["Speed traveled"] = speed
            report[x]["Fines"][count]["Fine"] = (fine)
            fileupdate()
            doNext = False
            #Changes the do next variable so the extra code which is not needed does not run


    #If plate cannot be found
    while doNext:
        choice = input("\nFile not found, create new file? Y/N: ")
        if choice.lower() == "y":

            #More data is needed to create the file, the data inputted is checked for errors
            driver = input("Enter drivers name: ")
            while driver.isalpha() == False: driver = input("Enter drivers name: ")
            dob = input("Enter drivers DOB in dd/mm/yyyy: ")
            #As there is no prior reports, the count variable does not need to be iterrated, it stays at 1
            count = "1"
            test = True
            while test:
                speedlim = input("Enter speed limit: ")
                if speedlim.isnumeric() == True:
                    if int(speedlim) < 160:
                        test = False

            speed = input("Enter speed: ")
            while speed.isnumeric() == False: speed = input("Enter speed: ")
            if int(speed) <= int(speedlim):
                print("Car was not speeding")
                doNext = False
                continue
            fine = input("Enter fine: £")
            while fine.isnumeric == False: fine = int(input("Enter fine: "))
            fine = ("£" + fine)

            #Data is appended and saved
            report[plate] = {}
            report[plate]["Driver"] = driver
            report[plate]["DOB"] = dob
            report[plate]["Fines"] = {}
            report[plate]["Fines"][count] = {}
            report[plate]["Fines"][count]["Speed limit"] = speedlim
            report[plate]["Fines"][count]["Speed traveled"] = speed
            report[plate]["Fines"][count]["Fine"] = fine
            fileupdate()

        elif choice.lower() != "n" and choice.lower() != "y":
            print("\nInvalid option")
        else:
            break
        break



def search():
    while True:
        search = input("\nEnter plate you wish to search: ")
        #Checks if license plate is in dictionary
        if search in report:
            #Prints out the raw data in a readable format
            #Each line is printed seperatly so it is easier to modify format

            fineamount = 0
            for x in report[search]["Fines"]:
                fineamount += 1

            print("\n\nLicense plate:",search,"\n")
            print("Driver:",report[search]["Driver"],"\tDOB:",report[search]["DOB"],"\tAmount of fines:",fineamount,"\n")
            #Prints out every violation the driver has
            for x in report[search]["Fines"]:
                print("Speed limit:",report[search]["Fines"][x]["Speed limit"],"\tSpeed traveled",report[search]["Fines"][x]["Speed traveled"],"\n\n")
                print("Fine Given:",report[search]["Fines"][x]["Fine"],"\n")
                print("---------------------------------------------\n")
        else: print("File could not be found")
        if input("Press 1 to quit: ") == "1": break





#Main
#Infinite loop that allows users to choose multiple options without resetting program
while True: 
    with open ("carfile.txt","r") as file:
        report = eval(file.read())

    choice = input("\n1)Add report\n2)View Files\n3)Exit\nEnter choice: ")
    if choice == "1": add()
    elif choice == "2": search()
    elif choice == "3": exit()
    else: print("Invalid choice")
