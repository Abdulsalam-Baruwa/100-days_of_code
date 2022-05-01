import random
from hangman_wordlist import word_list
from hangman_art import stages, logo

#onboarding
print(logo)
print("You have ❤ ❤ ❤ ❤ ❤ ❤  lives.\nFor every wrong guess made, you lose a life.")

#Create a variable called 'lives' to keep track of the number of lives left.
lives = 6

#Randomly choose a word from the word_list and assign it to a variable called chosen_word.
chosen_word = random.choice(word_list)

#Create an empty list called display.
display = []

for letter in chosen_word:
    display.append("_")
word_length = len(chosen_word)


end_game = False
while not end_game:
    guess = input("Guess a letter:\n").lower()
    if guess in display:
        print(f"You've already guessed {guess}.")

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word.\nYou lose a life!")
    
    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            end_game = True
            print("You Lose!")
    

    print(f"{' '.join(display)}")
    
    if "_" not in display:
        end_game = True
        print("You win!")
    
    print(stages[lives])