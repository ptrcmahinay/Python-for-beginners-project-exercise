import random
from hangman_word import word_list
from hangman_art import logo, stages

word_chosen = random.choice(word_list).lower()
word_length = len(word_chosen)
lives = 6

# for blanks
display = []
for _ in range(word_length):
    display += "_"

print(logo)
print(f"Word: {' '.join(display)}")

hint = input("Hint? (Y/N): ")
if hint == "Y":
    for clue in range(len(word_chosen)):
        one_clue = random.choice(clue)
    print(f"The clue is: {one_clue} ")
else: 
    end_of_game = False
    while not end_of_game:
        guess = input("Guess a letter: ").lower()
        if guess in display:
            print("You've already guessed a {guess}")
        
        # Checking guessed letters
        for position in range(len(word_chosen)):
            letter= word_chosen[position]
            if letter == guess:
                display[position] = letter

        #Join all the elements in the list and turn it into a String.
        print(f"{' '.join(display)}")

        # Checking if user is wrong
        if guess not in word_chosen:
            print(f"You guess {guess}, that's not in the word. You L O S T a life")
            lives -= 1
            if lives == 0:
                end_of_game = True
                print("You lose!")

        if "_" not in display:
            end_of_game = True
            print("You win!")
        
        print(stages[lives])
    
    
    
        

