import random
import numpy as np

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



# def random_card():
#     card = random.randint(2,14)
#     return card

def random_card(card_one, card_two, card_three=None):
    p_zero = 4/50
    p_card_one = 3/50
    p_card_two = 3/50
    p_card_three = 3/50
    p_list = []
    x = 0
    if card_one == card_two:
        p_card_one = 2/50
        p_card_two = 2/50
        
    if card_three:
        p_zero = 4/49
        p_card_one = 3/49
        p_card_two = 3/49
        p_card_three = 3/49

        if card_three == card_one and card_three == card_two:
            p_card_one = 1/49
            p_card_two = 1/49
            p_card_three = 1/49

        elif card_three == card_one:
            p_card_one = 2/49
            p_card_two = 3/49
            p_card_three = 2/49

        elif card_three == card_two:
            p_card_one = 3/49
            p_card_two = 2/49
            p_card_three = 2/49

        elif card_one == card_two:
            p_card_one = 2/49
            p_card_two = 2/49
            p_card_three = 3/49

    while x < 15:        
        if x == 0:
            p_list.append(0)
        elif x == 1:
            p_list.append(0)
        elif x == card_one:
            p_list.append(p_card_one)
        elif x == card_two:
            p_list.append(p_card_two)
        elif x == card_three:
            p_list.append(p_card_three)
        else:
            p_list.append(p_zero)
        x += 1

    card = np.random.choice(15, 1, p=p_list)  

    return card[0]