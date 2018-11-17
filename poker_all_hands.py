from winlist import get_win_pct_list_for_hand
import csv
import math
import numpy as np
import matplotlib.pyplot as plt
 
sampleSize = 1000
x_data = []
y_data = []
z_data = []

with open('SRP.csv', mode='w') as poker_file:  
    poker_writer = csv.writer(poker_file, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    poker_writer.writerow(['Card 1', 'Card 2', 'Win Procent'])  
    for x in range(2,15):
      for y in range(2,15): 
            win_list_x_y = get_win_pct_list_for_hand(x, y, sampleSize)
            win_pct = round(win_list_x_y[sampleSize - 1],2)
            poker_writer.writerow([x, y, win_pct])
            x_data.append(x)
            y_data.append(y)
            z_data.append(win_pct)
CS = plt.contourf([x_data, y_data], z_data, 100, cmap=plt.cm.rainbow, vmax=100, vmin=0)

plt.colorbar()
plt.show()

