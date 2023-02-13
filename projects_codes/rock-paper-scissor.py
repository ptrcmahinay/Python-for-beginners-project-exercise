# ROCK-PAPER-SCISSORS
import random

def play():
    player_score = 0
    computer_score = 0
    score_limit = 5
    attempts = 0
    attempts_limit = 3

    while player_score != score_limit and computer_score != score_limit:
        try:
            player = input("\nChoose a letter: \n\t'r' = rock\n\t's' = scissor \n\t'p' = paper \nEnter: ")
            computer = random.choice(['r', 's', 'p'])
        except ValueError:
            print("Please enter a letter from the choices")
        
        if player == computer:
            print("\n\nT I E\n")
            print(f"Your Score: {player_score}")
            print(f"Opponent Score: {computer_score}")
        
        elif (player == 'r' and computer == 's' or player == 's' and computer == 'p' or player == 'p' and computer == 'r'):
            print("\n\nCongratulations! YOU WON\n\n")
            player_score += 1
            print(f"Your Score: {player_score}")
            print(f"Opponent Score: {computer_score}")
            if player_score == score_limit:
                print("\n\n --------- YOU WON THE ROCK, PAPER AND SCISSOR ----------\n\n")
                if attempts <= attempts_limit:
                    play_again() 
                else:
                    print("You dont have enough chances to play again")
                    quit()
        else:
            print("\n\nOops! YOU LOSE :((\n\n")
            computer_score += 1
            print(f"Your Score: {player_score}")
            print(f"Opponent score:  {computer_score}")
            if computer_score == score_limit:
                print("\n\n --------- YOU LOSE THE ROCK, PAPER AND SCISSOR ----------\n\n")
                if attempts <= attempts_limit:
                    play_again()
                    
                else:
                    print("You dont have enough chances to play again")
                    quit()
        
        attempts += 1
                

def play_again():
    user_play_again_or_not = input(print("Do you want to play again? [Y/N]: "))
    if user_play_again_or_not == 'Y' or user_play_again_or_not == 'y':
        play()
    elif user_play_again_or_not == 'N' or user_play_again_or_not == 'n':
        print("\n THANK YOU FOR PLAYING!!")
        quit()
    else:
        print('Sorry, invalid input')

print(play())


