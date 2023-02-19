import random
from blackjack_art import the_logo

cards = [11, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
def deal_cards():
    """Returns a random cards from the deck"""
    return random.choice(cards)

user_cards = [deal_cards for _ in range(2)]
computer_cards = [deal_cards for _ in range(2)]

def calculate_score(cards):
    """Calculates the score of a list"""
    score = sum(cards)
    if score == 21 and len(cards) == 2:
        return 0
    elif score > 21 and 11 in cards:
        cards.remove(11)
        cards.append(1)
        return score
    return score

def compare_score(user_score, computer_score):
    """Compares the score of user_score with computer_score and returns the result"""
    if user_score == computer_score:
        return "It's a draw..."
    elif computer_score == 0:
        return "You lose."
    elif user_score == 0:
        return "You win. B L A C K J A C K"
    elif user_score > computer_score:
        return "You win."
    elif user_score > 21:
        return "You lose. You went over 21"
    elif computer_score > 21:
        return "You win. The computer went over 21"
    elif user_score < computer_score:
        return "You lose."

def play_game():
    """Plays a game of Blackjack"""
    user_cards = []
    computer_cards = []

    for _ in range(2):
        user_cards.append(deal_cards())
        computer_cards.append(deal_cards())
    
    game_end = False
    while not game_end:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"\tYour card: {user_cards}, current score: {user_score}")
        print(f"\tComputer card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            game_end = True
        else:
            draw_card = input("Type 'y' to get another card, type 'n' to pass: ").lower()
            if draw_card == 'y':
                user_cards.append(deal_cards())
            else:
                game_end = True
    
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_cards())
        computer_score = calculate_score(computer_cards)
    
    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare_score(user_score, computer_score))

while input("Do you want to play the game of Blackjack? type 'y' or 'n': ").lower() == 'y':
    print(the_logo)
    play_game()