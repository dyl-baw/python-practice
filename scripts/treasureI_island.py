print('''
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
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

direction = input("You're at a cross road. Where do you want to go? Type left or right\n")
direction_lower = direction.lower()

if direction == "right":
    print("Fall into a Hole. Game Over")
    quit()
else:
    swim = input('You have arrived at a lake. There is an island at the middle of the lake. Type "wait" to wait for a boat. Or type "swim" to swim to the lake.\n')
if swim == "swim":
    print("As you're swimming across, you're eaten by a giant fish. Game Over")
    quit()
else:
    arrive = input("You have taken the boat successfully to the island. There is a house with 3 doors. One red, one blue and one yellow. Which colour will you choose?\n").lower()
    # match arrive: // match / switch case requires python 3.10
    #     case "red":
    #         print("Burned by fire. Game Over.")
    #     case "blue":
    #         print("Eaten by beasts. Game Over.")
    #     case "yellow":
    #         print("You Win!")
    #     case _:
    #         print("Game Over.")

if arrive == "red":
    print("Burned by fire. Game Over.")
elif arrive == "blue":
    print("Eaten by beasts. Game Over.")
elif arrive == "yellow":
    print("You Win!")
else:
    print("Game Over.")
