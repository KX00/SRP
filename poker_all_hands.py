from winlist import get_win_pct_list_for_hand
import csv
import math
import numpy as np
import matplotlib.pyplot as plt

## Samplesize and data is initialized
sampleSize = 1000
data = np.array([])

## Open in csv (excel)
with open('SRP.csv', mode='w') as poker_file:  
    
    ## Create csv writer
    poker_writer = csv.writer(poker_file, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    ## Write headerrow (first line)
    poker_writer.writerow(['Card 1', 'Card 2', 'Win Procent'])  

    ## Create loop over x (card 1)
    for x in range(2,15):

      ## List of x constant and y in range 2-15 
      temp_data = []

      ## Create loop over y (card 2)
      for y in range(2,15): 

            ## Number of wins
            win_list_x_y = get_win_pct_list_for_hand(x, y, sampleSize)

            ## Winprocent with one decimal (last item of win_list)
            win_pct = round(win_list_x_y[sampleSize - 1],1)

            ## Write one row (x,y)
            poker_writer.writerow([x, y, win_pct])
          
            ## Add winpct to tempdata
            temp_data.append(win_pct)

      ## Np array
      np_temp_data = np.array([temp_data])

      
      if x == 2:
        data = np_temp_data
      else:
        data = np.concatenate((data, np_temp_data))

fig, ax = plt.subplots()
im = ax.imshow(data)

ax.set_xticks(np.arange(13))
ax.set_yticks(np.arange(13))

ax.set_xticklabels(np.arange(2,15))
ax.set_yticklabels(np.arange(2,15))

for i in range(13):
    for j in range(13):
        text = ax.text(j, i, data[i, j],
                       ha="center", va="center", color="w", size=7)

plt.show()


# plt.ylabel('Win Procent')
# plt.xlabel('Sample Size')
# plt.title('Sandsynlighed for at vinde en bestemt hånd i poker')