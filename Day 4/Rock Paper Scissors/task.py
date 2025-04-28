import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

moves = [rock, paper, scissors]
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors: \n"))
pc_choice = random.choice(moves)
if(user_choice >= 3 or user_choice < 0):
    print("Invalid choice. You lose.")
if(user_choice == 0):
    print(f"you chose: {rock} \n computer chose: {pc_choice}")
    if(pc_choice == rock):
        print("DRAW")
    elif(pc_choice == paper):
        print("YOU LOSE!")
    elif(pc_choice == scissors):
        print("YOU WIN!")

if(user_choice == 1):
    print(f"you chose: {paper} \n computer chose: {pc_choice}")
    if(pc_choice == rock):
        print("YOU WIN!")
    elif(pc_choice == paper):
        print("DRAW")
    elif(pc_choice == scissors):
        print("YOU LOSE")
if(user_choice == 2):
    print(f"you chose: {scissors} \n computer chose: {pc_choice}")
    if(pc_choice == rock):
        print("YOU LOSE!")
    elif(pc_choice == paper):
        print("YOU WIN!")
    elif(pc_choice == scissors):
        print("DRAW")