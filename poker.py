import random
import matplotlib
import matplotlib.pyplot as plt

class Winner:
    HAND_ONE = "HAND_ONE"
    HAND_TWO = "HAND_TWO"
    DRAW = "DRAW"

x = Winner.DRAW
print(x == Winner.DRAW)

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

hand_one_win_pct_list = []
hand_two_win_pct_list = []
draw_pct_list = []
xs = []

hand_one_win_count = 0
hand_two_win_count = 0
draw_count = 0

x = 0 
sampleSize = 100000

while x < sampleSize:
    hand_one_card_one = random_card()
    hand_one_card_two = random_card()
    hand_two_card_one = random_card()
    hand_two_card_two = random_card()

    winner = get_winner(11, 10, hand_two_card_one, hand_two_card_two)
    x += 1
    
    if winner == Winner.HAND_ONE:
        hand_one_win_count += 1
    
    if winner == Winner.HAND_TWO:
        hand_two_win_count += 1

    if winner == Winner.DRAW:
        draw_count += 1

    hand_one_win_pct = (hand_one_win_count/x)*100.00
    hand_two_win_pct = (hand_two_win_count/x)*100.00
    draw_pct = (draw_count/x)*100.00
    
    hand_one_win_pct_list.append(hand_one_win_pct)
    xs.append(x)

plt.plot(xs,hand_one_win_pct_list)
plt.ylim(0, 110)
plt.show()

 


#print('Hånd 1 har vundet','procent')
#print('Hånd 2 har vundet','procent')
#print('Draw har vundet', 'procent')

#x-akse hvor mange gange den har kørt
#y-akse procent vundende 
#3 nye lister
#loop skal glemme hvor mange er vundet
#af en hånd.