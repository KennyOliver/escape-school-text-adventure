from colorama import Fore, Back

def adventure():
  # Setup
  yes_no = ["yep", "nope"]
  directions = ['A','W','S','D']
  left_txt = "A | Left:\t\t"
  fwd_txt = "W | Forward:\t"
  rit_txt = "S | Right:\t\t"
  bhd_txt = "D | Behind:\t"
  
  # Introduction
  print("<-- ESCAPE SCHOOL!!! -->")
  name = input("What's your name?\n\t--> ")
  print(f"\nHey, {name}! Let's escape school!")
  print("You find yourself on the edge of the field.")
  print("Can you find your way out?\n")
  
  # STAGE 1
  response = ""
  while response not in yes_no:
    response = input("Would you like to climb over the fence?\nyep/nope\n").lower()
    if response == "yep":
      print("You climb over the fence, getting a few scrapes, but you managed to get out into the council estate.\n")
    elif response == "nope":
      print(f"Your\'e not ready for this.\nGoodbye, {name}!")
      return
    else: 
      print("I didn't understand that.\n")
  
  # STAGE 2
  response = ""
  while response not in directions:
    print(Fore.RED, f"{left_txt}a path leading somewhere...")
    print(Fore.LIGHTGREEN_EX, f"{fwd_txt}a small group of run-down bungalows")
    print(Fore.YELLOW, f"{rit_txt}a 10ft wooden fence")
    print(Fore.CYAN, f"{bhd_txt}the school")
    print(Fore.WHITE, "\n")
    response = input("What direction do you move? (A/W/S/D)\n\t--> ")
    if response == 'A':
      print(f"You get caught by a teacher on break duty.\nYOU LOSE, {name}!")
      return
    elif response == 'W':
      print("It's too high.\n")
      response = ""
    elif response == 'S':
      print("You head deeper into the council estate.\n")
      response = ""
    elif response == 'D':
      print(f"You leave the council estate. So long, {name}.")
      return
#====================
# MAIN PROGRAM
adventure()