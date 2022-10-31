
play = "y"
choice = input("Choice ")

if choice == "1":
    
    while play == "y":
        print("\nYour choices are:\nIron man\nHulk\nWonder Women\nSuper man\nBatman\nVision")

        if input("\nAre they male y/n ") == "n":
            print("Wonder women")
        else:
            
            if input("\nDo they have natural powers y/n ") == "n":

                if input("\nCan they fly y/n ") == "y":
                    print("Iron man")
                else:
                    print("Batman")
            else:
                if input("\nCan they fly y/n") == "n":
                    print("Hulk")
                else:
                    if input("Are they made of metal y/n ") == "n":
                        print("Superman")
                    else:
                        print("vision")
        play = input("\nplay again y\n ")  

                    
            
        
elif choice == "2":
    
    while play == "y":
        if input("\nDo you have weak legs y/n ") == "y":
            if input("\nDo you have weak upper legs y/n ") =="y":
                print("do Squat")
            else:
                print("do Calf Raise")
        else:
            if input("\nDo you have a weak back y/n ") =="y":
                print("do Pullups")
            else:
                if input("\nDo you have a weak chest y/n ") == "y":
                    print("do Bench press / push up")
                else:
                    if input("\nDo you have weak biceps or triceps b/t ") == "b":
                        print("do Curl")
                    else:
                        print("do Dips")
        play = input("\nplay again y/n ")

else:
    while play == "y":
        if input("Does it eat meat y/n: ") == "y":
            if input("Does it live in water y/n: ") == "y":
                if input ("Does it have spines on its back y/n: ") == "y":
                    print("spinasourus")
                else:
                    print("T rex")
            else:
                print("Mosasaurus")
        else:
            if input("Does it have 2 legs y/n: ") == "y":
                print("hadosaurus")
            else:
                if input("Does it have a long neck y/n: ") == "y":
                    print("Barosaurous")
                else:
                    print("Triceratops")


