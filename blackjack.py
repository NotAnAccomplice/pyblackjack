import random

# Define variables
current_player_hand = []
current_dealer_hand = []
game_state = 0
game_state_table = ["No winner has been decided","The player has won!","The player has lost..."]
# In this table, a game state of 1 means the player won (1 = won, heh)

# Define functions
def hit(hand):
    """
    Appends a random integer between (and including) 2 and 11 to a provided
    list hand, and then returns the list with the newly appended value.
    """
    hand.append(random.randint(2,11))
    return hand

def check_hand_sum(hand,dealer_or_player):
    # "player" is the presumed default for dealer_or_player.
    player_won = False
    player_lost = False

    if sum(hand) > 21:
        player_lost = True
    elif sum(hand) == 21:
        player_won = True

    # If the value of both player_won and player_lost are the same (both should be False), then the game_state should not change since no winner has been decided.
    if player_won == player_lost:
        game_state = 0
        return game_state

    # If the person playing is the dealer, then the result of player_won should be the opposite.
    if dealer_or_player == 'dealer':
        player_won = (not player_won)
        player_lost = (not player_lost)

    if player_won:
        game_state = 1
    elif player_lost:
        game_state = 2
    return game_state


def deal_starting_hand(player_hand, dealer_hand):
    """
    Runs the hit function twice to both the player and dealer hand. This
    results in both hands having two values.
    """
    for i in range(2):
        player_hand = hit(player_hand)
        dealer_hand = hit(dealer_hand)
    return player_hand, dealer_hand

def game_start_prints(player_hand, dealer_hand):
    """Prints statements for the user to read at the start of the game."""
    print("==========")
    print("Welcome to blackjack!")
    print("Cards have been dealt.")
    print("player's hand is: ", player_hand)
    print("dealer's visible hand is: ", dealer_hand[0])

def game_end_prints(game_state_table, game_state, player_hand, dealer_hand):
    """Prints statements for the user to read at the end of the game."""
    print(game_state_table[game_state])
    print("Final player hand is: ", player_hand)
    print("Which is a sum of: ", sum(player_hand))
    print("")
    print("Final dealer hand is: ", dealer_hand)
    print("Which is a sum of: ", sum(dealer_hand))

def player_turn(player_hand):
    """The player's turn. If the user inputs S, then stand (move to the dealer's turn). If the user inputs H, they have hit, and the loop continues unless their hand is greater than or equal to 21."""
    user_input = ""
    game_state = 0
    while user_input != 'S':
        print("")
        print("Your current hand is: ", player_hand)
        print("The current total of your hand is: ", sum(player_hand))

        user_input = input("Please enter 'H' for hit or 'S' for stand: ")
        user_input = user_input.upper()

        print("")

        if user_input not in ['H', 'S']:
            print("User did not put 'H' or 'S'!")
        if user_input == "H":
            print("Player hits!")
            player_hand = hit(player_hand)
        if user_input == "S":
            print("Player is standing. Ending player turn!")
            return game_state

        game_state = check_hand_sum(player_hand, "player")
        if game_state != 0:
            return game_state

def dealer_turn(dealer_hand, game_state):
    """The dealer's turn. If the dealer's hand sums to less than 17, she hits."""
    if game_state != 0:
        return game_state
    while sum(dealer_hand) < 17:
        dealer_hand = hit(dealer_hand)
    game_state = check_hand_sum(dealer_hand, "dealer")
    return game_state

def compare_player_and_dealer_hands(player_hand, dealer_hand, game_state):
    """Compares the player and dealer's hands. If the player's hand is greater, return game_state of 1 (player wins). Otherwise, return game_state 2 (player loses). This implies that in the event of a tie, the dealer wins."""
    if game_state != 0:
        return game_state
    if sum(player_hand) > sum(dealer_hand):
        game_state = 1
    else:
        game_state = 2
    return game_state

def main(player_hand, dealer_hand):
    """The main function which runs all others."""
    # Game Start!
    deal_starting_hand(player_hand, dealer_hand)
    game_start_prints(player_hand, dealer_hand)

    # Player and dealer turns!
    game_state = player_turn(player_hand)
    game_state = dealer_turn(dealer_hand, game_state)

    # Game end!
    game_state = compare_player_and_dealer_hands(player_hand, dealer_hand, game_state)
    game_end_prints(game_state_table, game_state, player_hand, dealer_hand)

if __name__ == '__main__':
    main(current_player_hand, current_dealer_hand)
