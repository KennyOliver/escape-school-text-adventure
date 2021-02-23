from colorama import Fore, Back

def adventure(input_money):
  wallet = input_money
  
  # STAGE 0
  response = ""
  while response not in yes_no:
    response = input("Would you like to climb over the fence? yep/nope\n\t--> ").lower()
    if response == "yep":
      print("\nYou climb over the fence, with a few scrapes, but you managed to get out into the council estate.")
      print(f"You found your wallet that someone threw over the fence last year!\nIt still has £{wallet}")
    elif response == "nope":
      print(f"You tried to get back inside the school, but a teacher caught you.\nGoodbye, {name}!")
      return
  
  # LEVEL 1
  print("A caretaker is walking towards the fence to see what the sound was!\n\nYou need to leave. QUICK!")
  response = ""
  print(Fore.YELLOW, f"{left_txt}a path leading somewhere...")
  print(Fore.LIGHTGREEN_EX, f"{fwd_txt}the council estate")
  print(Fore.CYAN, f"{rit_txt}a 10ft wooden fence")
  print(Fore.RED, f"{bhd_txt}the school", Fore.WHITE)
  while response not in directions:
    response = input("What do you choose? (A/W/S/D)\n\t--> ").upper()
  if response == 'A':
    print(f"You get caught by a teacher on break duty.\nYOU LOSE, {name}!\n\nPS: They bought some candy with your money.")
    return
  elif response == 'W':
    print("You head into the council estate, greeted by a £10 note on the ground!\n")
    wallet += 10
    see_wallet(wallet)
  elif response == 'S':
    print("It's too high.\n")
    wallet -= 5
    see_wallet(wallet)
    response = "" #restarts if-statement
  elif response == 'D':
    print(f"You chose detention.\nSo long, {name}!")
    return
  
  # LEVEL 2
  print("You see two roads ahead of you.")
  response = ""
  print(Fore.YELLOW, f"{left_txt}more terraced houses")
  print(Fore.CYAN, f"{rit_txt}a children\'s playground")
  print(Fore.WHITE, "\n")
  while response not in directions:
    response = input("What direction do you move? (A/W/S/D)\n\t--> ").upper()
  if response == 'A':
    print(f"You get caught by a teacher on break duty.\nYOU LOSE, {name}!")
    return
  elif response == 'W':
    print("You head deeper into the council estate.\n")
    wallet += 10
    see_wallet(wallet)
  elif response == 'S':
    print("It's too high.\n")
    money -= 5
    see_wallet(wallet)
    response = ""
  elif response == 'D':
    print(f"You leave the council estate. So long, {name}.")
    return
#====================
def see_wallet(amount):
  print(f"Wallet: £{amount}")
#====================
# MAIN PROGRAM
# Setup
yes_no = ["yep", "nope"]
directions = ['A','W','S','D']
left_txt = "A | Left:\t\t"
fwd_txt = "W | Forward:\t"
rit_txt = "S | Right:\t\t"
bhd_txt = "D | Behind:\t"
money = 1

# Introduction
print("<-- ESCAPE SCHOOL!!! -->")
name = input("What's your name?\n\t--> ")
print(f"\nHey, {name}! Let's escape school!")
print("You find yourself on the edge of the field.")
print("Can you find your way out?\n")

adventure(money)