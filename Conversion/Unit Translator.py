#IMPORT
import pandas as pd
units = ["millimeters","centimeters","meters","kilometers","inches","feet","yards","miles"]
cov_table = pd.read_csv("inCm.csv")



#FUNCTIONS
def convert_unit(old,amount,new,df,units):
    df = df.loc[df["units"] == old]
    conversion = (df[new])
    if units.index(old) >= units.index(new):
        amount = amount*conversion
    else:
        amount = amount/conversion
    return amount


        
    
    

#MAIN
while True:
    while True:
        try:
            unit = int(input("""\nEnter unit of measurement
1)Milimeter
2)Centimeter
3)Meter
4)Kilometer
5)Inch
6)Feet
7)Yard
8)Miles
Enter choice: """))
            if unit > 10 or unit < 1:
                print("\nPlease select in range")
            else:
                unit = units[unit-1]
                break
        except:
            print("\nPlease enter a number")
            


    while True:
        try:
            amount = float(input("\nEnter amount of " + unit + " : "))
            break
        except:
            print("\nPlease enter a number1")

            

    while True:
        try:
            convert = int(input("""\nEnter unit of conversion
1)Milimeter
2)Centimeter
3)Meter
4)Kilometer
5)Inch
6)Feet
7)Yard
8)Miles
Enter choice: """))
            
            if convert > 10 or convert < 1:
                print("\nPlease select in range")
            else:
                convert = units[convert-1]
                ans = convert_unit(unit,amount,convert,cov_table,units)
                print(ans)
                break
        
        except:
            print("\nPlease enter a number2")
        
