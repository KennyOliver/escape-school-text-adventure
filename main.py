def adventure():
  # Setup
  yes_no = ["yep", "nope"]
  directions = ['A','B','C','D']
  
  # Introduction
  name = input("What's your name?\n\t--> ")
  print(f"Hey, {name}! Let's escape school!")
  print("You find yourself on the edge of the field.")
  print("Can you find your way out?\n")
  
  # Start of game
  response = ""
  while response not in yes_no:
    response = input("Would you like to climb over the fence?\nyep/nope\n")
    if response == "yep":
      print("You climb over the fence, getting a few scrapes, but you managed to get out into the council estate.\n")
    elif response == "nope":
      print(f"Your\'e not ready for this.\nGoodbye, {name}!")
      return
    else: 
      print("I didn't understand that.\n")
     
    # Next part of game
    response = ""
    while response not in directions:
      print(Fore.RED, "A | To your left, you see a pathway leading somewhere...", Fore.WHITE)
      print(Fore.YELLOW, "B | To your right, you see a small group of run-down bungalows.", Fore.WHITE)
      print(Fore.LIGHTGREEN_EX, "C | There\'s a 10ft wooden fence directly in front of you.", Fore.WHITE)
      print(Fore.CYAN, "D | Behind you is the school.\n", Fore.WHITE)
      response = input("What direction do you move?\nA/B/C/D\n")
      if response == 'A':
        print("You get caught by a teacher on break duty. YOU LOSE, " + name + "!")
        return
      elif response == 'B':
        print("You head deeper into the council estate.\n")
        response = ""
      elif response == 'C':
        print("It's too high.\n")
        response = ""
      elif response == 'D':
        print(f"You leave the council estate. So long, {name}.")
        return
#====================
# MAIN PROGRAM
adventure()