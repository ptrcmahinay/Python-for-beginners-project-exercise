import random
from guessing_num_art import logo

# print the game logo
print(logo)
print("\t\tWelcome to the Number Guessing Game!\n")

# function to play the guessing game
def play_guess(attempts, ran_num):
    guess = 0
    # Keep running the loop until the player wins or runs out of attempts
    while guess != ran_num and attempts != 0:
        print(f"You have {attempts} attempts to guess")
        guess = int(input("Make a guess: "))
        # Check if the guess is higher or lower than the actual number
        if guess < ran_num:
            print("\nToo low\n") 
        elif guess > ran_num:
            print("\nToo high\n")
        # If the guess is correct, congratulate the player and end the game
        else:
            print(f"\n\tCongratulations! You have guessed the number {ran_num} correctly\n")
        attempts -= 1
    
    if attempts == 0 and guess != ran_num:
        print("YOU LOST")

def play_again():
    guess_again = input("Do you want to play guessing number again? Type 'yes' or 'no': ").lower()
    if guess_again == 'yes':
        main()
    else:
        exit()

def main():
    range_of_numbers = int(input("What is the range of numbers you want to guess? "))
    ran_num = random.randint(1,range_of_numbers)
    # print(ran_num) Will print the random number or answer
    level = input("\nChoose difficulty. Type 'easy' or 'hard': ").lower()
    if level == 'easy':
        attempts = 10
        play_guess(attempts, ran_num) 
    else:
        attempts = 5
        play_guess(attempts, ran_num)
    play_again()

main()

