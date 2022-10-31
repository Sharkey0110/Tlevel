import time

words = "some words to save"

def write():
    with open("data.txt","w") as file:
        file.write(words + "\n")
        file.close

def read():
    with open("data.txt","r") as file:
        file.close()

def append(filename,context):
    with open(filename + ".txt","a") as file:
        file.write("\n" + context)

def prepend(filename,context):
    with open(filename + ".txt","a") as file:
        file.seek(0)
        file.append("\n" + context)

write()
(append(input("Enter file name: "),input("Enter context: ")))
(prepend(input("Enter file name: "),input("Enter context: ")))


