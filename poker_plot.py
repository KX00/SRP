import matplotlib
import matplotlib.pyplot as plt
from winlist import get_win_pct_list_for_hand

sampleSize = 1000

win_list_5_6 = get_win_pct_list_for_hand(5, 6, sampleSize)
print(win_list_5_6[sampleSize - 1])
win_list_10_9 = get_win_pct_list_for_hand(10, 9, sampleSize)
print(win_list_10_9[sampleSize - 1])
win_list_8_8 = get_win_pct_list_for_hand(8, 8, sampleSize)
print(win_list_8_8[sampleSize - 1])

xs = list(range(1, sampleSize+1))

#plt.hlines(y=100, xmin=0, xmax=sampleSize, colors='k', linestyles='solid', data=None)
plt.ylabel('Win Procent')
plt.xlabel('Sample Size')
plt.title('Sandsynlighed for at vinde en bestemt hånd i poker')
p1 = plt.plot(xs,win_list_5_6)
p2 = plt.plot(xs,win_list_10_9)
p3 = plt.plot(xs,win_list_8_8)
plt.legend((p1[0], p2[0], p3[0]), ('Cards 5 and 6', 'Cards 10 and 9', 'Pair 8'))
plt.ylim(0, 130)
plt.show()

#print('Hånd 1 har vundet','procent')
#print('Hånd 2 har vundet','procent')
#print('Draw har vundet', 'procent')
 
#x-akse hvor mange gange den har kørt
#y-akse procent vundende 
#3 nye lister
#loop skal glemme hvor mange er vundet
#af en hånd