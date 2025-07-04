print(r'''

       {}           {}
         \  _---_  /
          \/     \/
           |() ()|
            \ + /
           / HHH  \
          /  \_/   \
        {}          {}
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
                                                       {}           {}
                                                         \  _---_  /
                                                          \/     \/
                                                           |() ()|
                                                            \ + /
                                                           / HHH  \
                                                          /  \_/   \
                                                        {}          {}
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
direction = input('You\'re at a crossroad. Where you want to go? \n Type "left" or "right" \n').strip().lower()

if direction == "left":
    action = input('You\'ve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across \n').strip().lower()
    if action == "wait":
        door = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose? \n").strip().lower()
        if door == "red":
            print("It's a room full of fire. GAME OVER!")
        elif door == "blue":
            print("It's a room full of starved mythical beasts. GAME OVER!")
        elif door == "yellow":
            print("You found the treasure! YOU WIN!")
        else:
            print("\nOopsie! Invalid input")
    elif action == "swim":
        print("Attacked by angry sharks. GAME OVER!")
    else:
        print("\nOopsie! Invalid input")
elif direction == "right":
    print("\nYou fell into a hole. GAME OVER!")
else:
    print("\nOopsie! Invalid input")
