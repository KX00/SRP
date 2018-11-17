import random

class Winner:
    HAND_ONE = 1
    HAND_TWO = 2
    DRAW = 3

x = Winner.DRAW
print(x == Winner.DRAW)

def compare_pairs(hand_one_has_pair, hand_two_has_pair, hand_one_card_one, hand_two_card_one):
    if hand_one_has_pair:
        if hand_two_has_pair:
            if hand_one_card_one > hand_two_card_one:
                return True
            else:
                return False
        else:
            return True
    else:
        if hand_two_has_pair:
            return False

def high_card(hand_one_card_one, hand_one_card_two, hand_two_card_one, hand_two_card_two):
    #highst card highst kicker
    hand_one_max = max(hand_one_card_one, hand_one_card_two)
    hand_two_max = max(hand_two_card_one, hand_two_card_two)

    if hand_one_max > hand_two_max:
        return True
    
    elif hand_one_max == hand_two_max:
        hand_one_min = min(hand_one_card_one, hand_one_card_two)
        hand_two_min = min(hand_two_card_one, hand_two_card_two)

        if hand_one_min > hand_two_min:
            return True

    return False

def hand_one_wins(hand_one_card_one, hand_one_card_two, hand_two_card_one, hand_two_card_two):
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

hand_one_win_count = 0

x = 0 
sampleSize = 10000 

while x < sampleSize:
    hand_one_card_one = random_card()
    hand_one_card_two = random_card()
    hand_two_card_one = random_card()
    hand_two_card_two = random_card()

    win = hand_one_wins(11, 10, hand_two_card_one, hand_two_card_two)
    x += 1

    if win:
        hand_one_win_count += 1
print('Du har vundet', hand_one_win_count, 'gange')