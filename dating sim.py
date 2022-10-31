#IMPORTS
import random 
import time

#FUNCTIONS

def PastdayAi():
    time = random.randint(1,12)
    time2 = ["AM","PM"]
    date = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday",]
    place = ["movies","shops","gym","park","restraunt","Swimming pool","museum","busstop","town centre","beach","mountains","lodge"]
    print("At " + str(time) + (random.choice(time2) + " last " + random.choice(date) + " I went to the " + random.choice(place)))
    global relpoints
    
    answer = input("\nA: That sounds fun \nB: We should go together sometime \nC: Thats so mid \nWhat do you think?: ")

    if answer == "A":
          print("Yeah, it was!\n")
          relpoints += 2
          return relpoints  
    elif answer == "B" and relpoints >= 25:
          print("I'd like that\n")
          relpoints += 6
          return relpoints  
    elif answer == "B" and relpoints < 25:
          print("hmmm, maybe some other time\n")
          relpoints -=3
          return relpoints   
    else:
          print("Your so mean\n")
          relpoints -= 7
          return relpoints





    
def planAi():
     global relpoints
     time = random.randint(1,12)
     time2 = ["AM","PM"]
     date = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday",]
     place = ["movies","shops","gym","park","restraunt","Swimming pool","museum","busstop","town centre","beach","mountains","lodge"]
     print("How about at " + str(time) + "next " + random.choice(date) + " we should go to the " + random.choice(place))
     answer2 = input("\nA: We should \nB: Nah im busy \nWhat do you think: ")
     if answer2 == "A":
         relpoints +=1
         answer = input("That was fun! Did you enjoy yourself? \nA:Yeah I did \nB: Wasnt a fan\nWhat do you think: ")
         if answer == "A":
             print("Yay")
             relpoints += 7
         else:
             print("Oh")
             relpoints -=12
     else:
        print("Oh thats alright ig")
        relpoints -= 4
                
         
     

def smalltalk():
    global relpoints
    topic1 = ["What is your favourite ","What is your least favourite "]
    topic2 = ["food ","music band ","drink ",]
    print(random.choice(topic1) + random.choice(topic2))
    input()
    print("Intresting choice!\n ")
    relpoints += 1
    
    

    
#MAIN
relpoints = 0
while relpoints <10:
    smalltalk()

while relpoints >=10 and relpoints < 25:
    smalltalk()
    PastdayAi()

while relpoints >=25:
    smalltalk()
    PastdayAi()
    planAi()
    
        
    
    


