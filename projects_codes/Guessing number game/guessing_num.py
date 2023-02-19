import random
from guessing_num_art import logo

ran_num = random.randint(1, 100)
print(logo)
print("\t\tWelcome to the Number Guessing Game!\n")
print("I'm thinking of a number between 1 to 100")
# print(ran_num)

def play_guess(attempts):
    guess = 0
    while guess != ran_num and attempts != 0:
        print(f"You have {attempts} attempts to guess")
        guess = int(input("Make a guess: "))
        if guess < ran_num:
            attempts -= 1
            print("\nToo low\n") 
        elif guess > ran_num:
            attempts -= 1
            print("\nToo high\n")
        else:
            print(f"\n\tCongratulations! You have guessed the number {ran_num} correctly\n")

def play_again():
    guess_again = input("Do you want to play guessing number again? Type 'yes' or 'no': ").lower()
    if guess_again == 'yes':
        main()
    else:
        exit()

def main():
    level = input("\nChoose difficulty. Type 'easy' or 'hard': ").lower()
    if level == 'easy':
        attempts = 10
        play_guess(attempts)
        
    else:
        attempts = 5
        play_guess(attempts)
    play_again()

main()



 

# def play():
#     level = input("Choose difficulty. Type 'easy' or 'hard': ").lower()
#     if level == 'easy':
#         attempts = 10
#         guess = 0
#         while guess != ran_num:
#             print(f"You have {attempts} attempts to guess")
#             guess = int(input("Make a guess: "))
#             if guess < ran_num:
#                 print("Too low")
#                 
#             elif guess > ran_num:
#                 print("Too high")
#                 
#             else:
#                 print(f"Congratulations! You have guessed the number {ran_num} correctly")
#     else:
#         attempts = 5
#         guess = 0
#         while guess != ran_num:
#             print(f"You have {attempts} attempts to guess")
#             guess = int(input("Make a guess: "))
#             if guess < ran_num:
#                 print("Too low")
#                 
#             elif guess > ran_num:
#                 print("Too high")
#                 
#             else: 
#                 print(f"Congratulations! You have guessed the number {ran_num} correctly")
# play()   

        
    
        
        

        
