
import os
import random 
from hangman_art import logo, stages

print(logo)
print("Welcome to Hang Man. \nYou will have 6 opportunities to guess the word.")

from hangman_words import word_list

game_complete = False
chosen_word = random.choice(word_list)

length_of_word = len(chosen_word)
display = []
for _ in range(length_of_word):
    display += "_"
print(display)


lives = 6


while not game_complete:
    guess = input("Guess a letter: ").lower()

    os.system('cls')

    if guess in display:
      print(f"You've already guessed {guess}")

    for position in range(length_of_word):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed {guess}, the letter is not in the word. You lose a life. \nYou have {lives} lives left.")
        if lives == 0:
            game_complete = True
            print("You lose.")
    
    print(f"{' '.join(display)}")

    if "_" not in display:
        game_complete = True
        print("You win.")
    
    print(stages[lives])