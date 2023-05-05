import random
numberOfStreaks = 0
for experimentNumber in range(10000):
    # Code that creates a list of 100 'heads' or 'tails' values.
    flips = []
    flipCounter = 0
    i = 0
    while i < 100:     
        if random.randint(0, 1) == 0:
            flips.append('T')
        else: 
            flips.append('H')
        i += 1
    # Code that checks if there is a streak of 6 heads or tails in a row. 
    streakCounter = 1
    for i in range(1, len(flips)):
        if flips[i] == flips[i-1]:
            streakCounter += 1
            if streakCounter == 6:
                numberOfStreaks += 1
                break
        else:
            streakCounter = 1          

print('Chance of streak: %s%%' % (numberOfStreaks / (100*10000)))