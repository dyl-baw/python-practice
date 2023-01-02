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

#Write your code below this line 👇

#declaring choices for the game.
rps = [rock, paper, scissors]
MAX_CHOICE = 3 

user_prompt = input("What will you choose? Type 0 for Rock, 1 for Paper for 2 for Scissors. \n")
#Error checking the User input
if int(user_prompt) >= 3 or int(user_prompt) < 0:
    print("You've typed an invalid number. You've lost!")
else:
    #Computer logic
    user_choice = rps[int(user_prompt)]
    random_generator = random.randint(0, MAX_CHOICE - 1)
    computer_choice = rps[random_generator]
    print(user_choice)
    print("Computer Chose: ")
    print("\n" + computer_choice)
    #Game logic
    if user_choice == 0 and computer_choice == 2:
        print("You lose!")
    elif user_choice == 2 and computer_choice == 0:
        print("You win!")
    elif user_choice > computer_choice:
        print("You win!")
    elif computer_choice > user_choice:
        print("You lose!")
    elif user_choice == computer_choice:
        print("Draw")

