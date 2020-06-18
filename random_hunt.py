# More experimenting with 'random' walks

# Import libraries
import numpy as np
import random
import matplotlib.pyplot as plt
import math 

def random_hunt():
    """Hunt with random walk"""

    m = 100 # length and width of search space
    food_num = int(math.log(m)) # number of pieces of food in search space
    A = np.zeros((m,m))
    
    # Place food in search space
    for i in range(1,food_num + 1):
        x_cord = random.randint(0,m-1)
        y_cord = random.randint(0,m-1)
        
        A[x_cord][y_cord] += 1 # value of 1 represents food is present
        
    # Place predator in search space
    pred_path = [] # list of all cells predator visits
            
    x_cord = random.randint(0,m-1)
    y_cord = random.randint(0,m-1)
    
    pred_path.append((x_cord, y_cord))
         
    # Let the hunt begin
    hunt_bool = True
    
    while (hunt_bool):
        x_step = (-1)**(random.randint(1,2))*random.randint(1,m)
        y_step = (-1)**(random.randint(1,2))*random.randint(1,m)
        
        current_x = (pred_path[-1][0] + x_step)%(m-1) # mod wraps path
        current_y = (pred_path[-1][1] + y_step)%(m-1) #
        
        pred_path.append((current_x, current_y))
        
        if (A[current_x][current_y] != 0):
            hunt_bool = False
          
    """
    # Plot the hunt
    plt.plot(*zip(*pred_path))
    plt.title(f'Food found in {len(pred_path) - 1} steps')
    plt.show()
    plt.close()
    """
    
    return (1 - (len(pred_path) - 1)/(m**2))

steps = [] # store steps to find food with random walk
for i in range(1,1001):
    steps.append(random_hunt())
    
print(f'iterations: {len(steps)}, mean score: {np.mean(steps)}')
