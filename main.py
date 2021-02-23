def adventure():
        # Setup
    yes_no = ["yep", "nope"]
    directions = ["A", "B", "C", "D"]
     
    # Introduction
    name = input("What's your name?\n")
    print("Hey, " + name + ". Let's escape school!")
    print("You find yourself on the edge of the field.")
    print("Can you find your way out?\n")
     
    # Start of game
    response = ""
    while response not in yes_no:
        response = input("Would you like to climb over the fence?\nyep/nope\n")
        if response == "yep":
            print("You climb over the fence, getting a few scrapes, but you managed to get out into the council estate.\n")
        elif response == "nope":
            print("You are not ready for this quest. Goodbye, " + name + ".")
            return
        else: 
            print("I didn't understand that.\n")
     
    # Next part of game
    response = ""
    while response not in directions:
        print(Fore.RED, "A | To your left, you see a pathway leading somewhere...", Fore.WHITE)
        print(Fore.YELLOW, "B | To your right, you see a small group of run-down bungalows.", Fore.WHITE)
        print(Fore.LIGHTGREEN_EX, "C | There is a 10ft wooden fence directly in front of you.", Fore.WHITE)
        print(Fore.CYAN, "D | Behind you is the main road.\n", Fore.WHITE)
        response = input("What direction do you move?\nA/B/C/D\n")
        if response == "A":
            print("You get caught by a teaching on break duty. YOU LOSE, " + name + "!")
            return
        elif response == "B":
            print("You head deeper into the council estate.\n")
            response = ""
        elif response == "C":
            print("You can't climb over.\n")
            response = "" 
        elif response == "D":
            print("You leave the estate. Bye, " + name + ".")
            return
        '''elif response == "/cheat":
          print("YOUV'E WON!")
          exit()'''
        #else:
            #print("I didn't understand that.\n")
  
adventure()