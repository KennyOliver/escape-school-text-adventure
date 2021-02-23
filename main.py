from colorama import Fore, Back

def adventure(money):
  # STAGE 1
  response = ""
  while response not in yes_no:
    response = input("Would you like to climb over the fence? yep/nope\n\t--> ").lower()
    if response == "yep":
      print("You climb over the fence, with a few scrapes, but you managed to get out into the council estate.\n")
    elif response == "nope":
      print(f"You tried to get back inside the school, but a teacher caught you.\nGoodbye, {name}!")
      return
  
  # STAGE 2
  response = ""
  print(Fore.RED, f"{left_txt}a path leading somewhere...")
  print(Fore.LIGHTGREEN_EX, f"{fwd_txt}a small group of run-down bungalows")
  print(Fore.YELLOW, f"{rit_txt}a 10ft wooden fence")
  print(Fore.CYAN, f"{bhd_txt}the school")
  print(Fore.WHITE, "\n")
  while response not in directions:
    response = input("What direction do you move? (A/W/S/D)\n\t--> ").upper()
  if response == 'A':
    print(f"You get caught by a teacher on break duty.\nYOU LOSE, {name}!")
    return
  elif response == 'W':
    print("You head deeper into the council estate.\n")
    money += 10
    get_money()
  elif response == 'S':
    print("It's too high.\n")
    money -= 5
    get_money()
    response = "" #restarts if-statement
  elif response == 'D':
    print(f"You leave the council estate. So long, {name}.")
    return
  
  # STAGE 3
  print("You see two roads ahead")
  response = ""
  print(Fore.RED, f"{left_txt}a patho leading somewhere...")
  print(Fore.LIGHTGREEN_EX, f"{fwd_txt}a small group of run-down bungalows")
  print(Fore.YELLOW, f"{rit_txt}a 10ft wooden fence")
  print(Fore.CYAN, f"{bhd_txt}the school")
  print(Fore.WHITE, "\n")
  while response not in directions:
    response = input("What direction do you move? (A/W/S/D)\n\t--> ").upper()
  if response == 'A':
    print(f"You get caught by a teacher on break duty.\nYOU LOSE, {name}!")
    return
  elif response == 'W':
    print("It's too high.\n")
    response = ""
  elif response == 'S':
    print("You head deeper into the council estate.\n")
  elif response == 'D':
    print(f"You leave the council estate. So long, {name}.")
    return
#====================
def get_money():
  print(f"Wallet: £{money}")
#====================
# MAIN PROGRAM
# Setup
yes_no = ["yep", "nope"]
directions = ['A','W','S','D']
left_txt = "A | Left:\t\t"
fwd_txt = "W | Forward:\t"
rit_txt = "S | Right:\t\t"
bhd_txt = "D | Behind:\t"
money = 0

# Introduction
print("<-- ESCAPE SCHOOL!!! -->")
name = input("What's your name?\n\t--> ")
print(f"\nHey, {name}! Let's escape school!")
print("You find yourself on the edge of the field.")
print("Can you find your way out?\n")

adventure(money)