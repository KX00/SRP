from poker_hands_compare import random_card
import numpy as np
import matplotlib.pyplot as plt

sampleSize = 100000.00
data = []
x = 0


while x < sampleSize:
    x += 1
    card = random_card(6,5,4)
    data.append(card)

# the histogram of the data
n, bins, patches = plt.hist(data, 26, density=False, facecolor='g', alpha=0.75)


plt.xlabel('Kort nummer')
plt.ylabel('Antal observationer')
plt.title('Fordeling for tilfældig kort')
plt.axis([1, 15, 0, sampleSize/10])
plt.grid(True)
plt.show()