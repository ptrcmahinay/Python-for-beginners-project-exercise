import random

# ASCII art for rock, paper, and scissors
ROCK = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

PAPER = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

SCISSORS = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

OPTIONS = [ROCK, PAPER, SCISSORS,]
SCORE_LIMIT = int(input("What is the score limit? "))


def scoring(player_score, computer_score):
    """Prints the current score of the player and computer.

    Args:
        player_score (int): The current score of the player.
        computer_score (int): The current score of the computer.
    """
    print("---------------------------------------")
    print(f"Your Score: {player_score}")
    print(f"Computer Score: {computer_score}")
    print("---------------------------------------\n")


def battle():
    """Starts the game and allows the player to play against the computer until one player reaches the score limit."""
    player_score = 0
    computer_score = 0

    while SCORE_LIMIT !=  player_score and computer_score != SCORE_LIMIT:
        player = int(input("What do you choose? \n\t0 for Rock \n\t1 for Paper \n\t2 for Scissors:\n "))
        if player not in range(3):
            print("Invalid input. Please enter a number between 0 and 2.")
            continue
        
        print(OPTIONS[player])
        computer = random.randint(0, 2)
        print("Computer chose: ")
        print(OPTIONS[computer])

        if player == computer:
            print("Draw")
            scoring(player_score, computer_score)
            
        # r > s, s > p, p > r 
        elif (player == 0 and computer == 2) or ( player == 2 and computer == 1) or (player == 1 and computer == 0):
            print("YEY, you won!!")
            player_score += 1
            scoring(player_score, computer_score)
            if (player_score == SCORE_LIMIT):
                print("\n\n --------- YOU WON THE ROCK, PAPER AND SCISSOR ----------\n\n")
                play_again()
        else:
            print("You lost!")
            computer_score += 1
            scoring(player_score, computer_score)
            if computer_score == SCORE_LIMIT:
                print("\n\n --------- YOU LOST THE ROCK, PAPER AND SCISSOR ----------\n\n")
                play_again()


def play_again():
    """Allows the user to play the game again or quit the game."""
    while True:
        user_play_again_or_not = input("Do you want to play again? Yes or No?: ").lower()
        if user_play_again_or_not == 'yes':
            battle()
        elif user_play_again_or_not == 'no':
            print("\n THANK YOU FOR PLAYING!!")
            quit()
        else:
            print('Sorry, invalid input')
            continue


battle()