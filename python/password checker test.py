#FUNCTIONS
def lencheck():
    while True:
        global password
        password = input("Enter a new password: ")

        if len(password) > 12:
            print("Your password is too big, try again")
        elif len(password) < 6:
            print("Your password is too small, try again")
        elif "'" in password or '"' in password:
            print("No SQL please")
        else:
            return(password)
            break
    

#MAIN
lencheck()
while True:
    S = 0
    for x in password:
        if x.isalpha():
            
            for x in password:
                if x == x.upper()and x.isalpha():
                    S += 1
                    break

                
            for x in password:
                if x == x.lower()and x.isalpha():
                    S += 1
                    break
                
            for x in password:
                if not x.isalpha():
                    S+=1
                    break
                


            for x in password:
                if x in ["0","1","2","3","4","5","6","7","8","9"]:
                    S += 1
                    break

                

            if S == 1:
                print("The password inputted is valid, but is a weak password")
                exit()
                
                
            elif S == 2:
                print("The password inputted is valid, it has medium security")
                exit()
                
                
            else:
                print("The password inputted is valid and it is a strong password!")
                exit()

    
    print("Invalid")
    lencheck()
    
    
    
                

        
            





            
    
                
            



        










