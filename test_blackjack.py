import blackjack
import mock
import builtins

def test_gameStart_howManyCardsDealt_twoCardDealt():
    player_hand = []
    dealer_hand = []
    player_hand, dealer_hand = blackjack.deal_starting_hand(player_hand, dealer_hand)
    assert len(player_hand) == 2
    assert len(dealer_hand) == 2

def test_gameStart_howManyDealerCardsVisible_onlyOneDealerCardVisible():
    player_hand = []
    dealer_hand = []
    player_hand, dealer_hand = blackjack.deal_starting_hand(player_hand, dealer_hand)
    # I'm using dealer_hand[0] as the value shown to the player as the dealer's hand. If its datatype is list rather tan int, we have a problem.
    assert isinstance(dealer_hand[0], int)

def test_hit_onHit_oneCardDealt():
    player_hand = []
    blackjack.hit(player_hand)
    assert len(player_hand) == 1

def test_main_gameState_isNotDataTypeNoneByEnd():
    with mock.patch.object(builtins, 'input', lambda _ : 's'):
        player_hand = [1,1]
        game_state = 0
        game_state = blackjack.player_turn(player_hand)
        assert isinstance(game_state, int)

def test_dealer_turn_whenDealerGetsOver16_sheHits():
    """In this test, the dealer starts with a hand of 16. So when it's their
    turn, they should hit, get any card, and then stand, leading to a hand of three
    cards (i.e. len(dealer_hand) == 3)."""
    dealer_hand = [10,6]
    game_state = 0
    blackjack.dealer_turn(dealer_hand, game_state)
    assert (len(dealer_hand) == 3)

def test_check_hand_sum_ifPlayerHandIsGreaterThan21_setGameStateTo2():
    hand = [20,2]
    dealer_or_player = "player"
    game_state = blackjack.check_hand_sum(hand, dealer_or_player)  
    assert game_state == 2

def test_check_hand_sum_ifPlayerHandIsEqualTo21_setGameStateTo1():
    hand = [20,1]
    dealer_or_player = "player"
    game_state = blackjack.check_hand_sum(hand, dealer_or_player)  
    assert game_state == 1

def test_check_hand_sum_ifPlayerHandIsLessThan21_setGameStateTo0():
    hand = [19,1]
    dealer_or_player = "player"
    game_state = blackjack.check_hand_sum(hand, dealer_or_player)  
    assert game_state == 0

def test_check_hand_sum_ifDealerHandIsGreaterThan21_setGameStateTo1():
    hand = [20,2]
    dealer_or_player = "dealer"
    game_state = blackjack.check_hand_sum(hand, dealer_or_player)  
    assert game_state == 1

def test_check_hand_sum_ifDealerHandIsEqualTo21_setGameStateTo2():
    hand = [20,1]
    dealer_or_player = "dealer"
    game_state = blackjack.check_hand_sum(hand, dealer_or_player)  
    assert game_state == 2

def test_check_hand_sum_ifDealerHandIsLessThan21_setGameStateTo0():
    hand = [19,1]
    dealer_or_player = "dealer"
    game_state = blackjack.check_hand_sum(hand, dealer_or_player)  
    assert game_state == 0

# The following tests set player_hand equal to a list that will sum up to 19 or
# eighteen, but have a different length than the dealer hand. This is to ensure
# that the sum functionality is in place, and that we are not accidentally
# doing direct list comparison (i.e., we are doing `sum(player_hand) >
# sum(dealer_hand)` rather than `player_hand > dealer_hand`)
def test_compare_player_and_dealer_hands_ifPlayerHandGreaterThanDealer_setGameStateTo1():
    player_hand = [10,9,1]
    dealer_hand = [18,1]
    game_state = 0
    game_state = blackjack.compare_player_and_dealer_hands(player_hand, dealer_hand, game_state)
    assert game_state == 1

def test_compare_player_and_dealer_hands_ifPlayerHandEqualToDealer_setGameStateTo2():
    player_hand = [10, 9, 1]
    dealer_hand = [19,1]
    game_state = 0
    game_state = blackjack.compare_player_and_dealer_hands(player_hand, dealer_hand, game_state)
    assert game_state == 2

def test_compare_player_and_dealer_hands_ifPlayerHandLessThanDealer_setGameStateTo2():
    player_hand = [10, 8,1]
    dealer_hand = [19,1]
    game_state = 0
    game_state = blackjack.compare_player_and_dealer_hands(player_hand, dealer_hand, game_state)
    assert game_state == 2
