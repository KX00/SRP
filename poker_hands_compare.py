import random

class Winner:
    HAND_ONE = "HAND_ONE"
    HAND_TWO = "HAND_TWO"
    DRAW = "DRAW"

def compare_pairs(hand_one_has_pair, hand_two_has_pair, hand_one_card_one, hand_two_card_one):
    if hand_one_has_pair:
        if hand_two_has_pair:
            if hand_one_card_one > hand_two_card_one:
                return Winner.HAND_ONE
            else:
                return Winner.HAND_TWO
        else:
            return Winner.HAND_ONE
    else:
        if hand_two_has_pair:
            return Winner.HAND_TWO

def high_card(hand_one_card_one, hand_one_card_two, hand_two_card_one, hand_two_card_two):
    #highst card highst kicker
    hand_one_max = max(hand_one_card_one, hand_one_card_two)
    hand_two_max = max(hand_two_card_one, hand_two_card_two)

    if hand_one_max > hand_two_max:
        return Winner.HAND_ONE
    
    elif hand_one_max == hand_two_max:
        hand_one_min = min(hand_one_card_one, hand_one_card_two)
        hand_two_min = min(hand_two_card_one, hand_two_card_two)

        if hand_one_min > hand_two_min:
            return Winner.HAND_ONE
        
        if hand_one_min == hand_two_min:
            return Winner.DRAW

    return Winner.HAND_TWO

def get_winner(hand_one_card_one, hand_one_card_two, hand_two_card_one, hand_two_card_two):
    #print(hand_one_card_one, hand_one_card_two, hand_two_card_one, hand_two_card_two)

    #check for pair
    hand_one_has_pair = hand_one_card_one == hand_one_card_two
    hand_two_has_pair = hand_two_card_one == hand_two_card_two
    if hand_one_has_pair or hand_two_has_pair:
        return compare_pairs(hand_one_has_pair, hand_two_has_pair, hand_one_card_one, hand_two_card_one)

    return high_card(hand_one_card_one, hand_one_card_two, hand_two_card_one, hand_two_card_two)

def random_card():
    card = random.randint(2,14)
    return card