from poker_hands_compare import random_card, get_winner, Winner
def get_win_pct_list_for_hand(hand_one_card_one, hand_one_card_two,sampleSize):

    hand_one_win_pct_list = []
    #hand_two_win_pct_list = []
    #draw_pct_list = []
    xs = []

    hand_one_win_count = 0
    hand_two_win_count = 0
    draw_count = 0

    x = 0 


    while x < sampleSize:
        hand_two_card_one = random_card(hand_one_card_one, hand_one_card_two)
        hand_two_card_two = random_card(hand_one_card_one, hand_one_card_two, hand_two_card_one)
        winner = get_winner(hand_one_card_one, hand_one_card_two, hand_two_card_one, hand_two_card_two)
        x += 1
        
        if winner == Winner.HAND_ONE:
            hand_one_win_count += 1
        
        if winner == Winner.HAND_TWO:
            hand_two_win_count += 1

        if winner == Winner.DRAW:
            draw_count += 1

        hand_one_win_pct = (hand_one_win_count/x)*100.00
       #hand_two_win_pct = (hand_two_win_count/x)*100.00
      #  draw_pct = (draw_count/x)*100.00
        
        hand_one_win_pct_list.append(hand_one_win_pct)
        xs.append(x)

    return hand_one_win_pct_list