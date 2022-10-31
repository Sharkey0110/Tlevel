from prettytable import PrettyTable


mytable = PrettyTable(names = ["Is it mutable", "Can size change", "Can items change","How many data types can be stored"])

mytable.add_row(["Lists","y", "y", "y", "Can store multiple data types"])
mytable.add_row(["Arrays","y", "n", "y","Can store similar data types"])
mytable.add_row(["Tuples","n", "n", "n","Can store multiple data types"])




print(mytable)


listint = ["3", "5", "6", "10", "12"]
liststr = ["Hello", "hi", "hey", "up", "down"]
print(listint)
print(liststr)
listint.reverse()
liststr.reverse()
print(listint)
print(liststr)
listint.reverse()
liststr.reverse()
print(liststr + listint)

for x in range(len(listint)):
    print(int(listint[x])**2)
    
