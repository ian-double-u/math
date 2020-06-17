# Experimenting with 'random' walks

# Import libraries
import numpy as np
import random
import matplotlib.pyplot as plt
import math


# Set up grid
n = 100000 # number of steps in walk

x = np.zeros(n) # initializing grid
y = np.zeros(n) #

# Filling grid
for i in range(1,n):
    direction = random.randint(1, 4)
    step_size = random.randint(1, 4)
    
    if (direction == 1): # x-left
        x[i] = x[i - 1] - step_size
        y[i] = y[i - 1] 
        
    elif (direction == 2): # x-right
        x[i] = x[i - 1] + step_size
        y[i] = y[i - 1] 
        
    elif (direction == 3): # y-down
        x[i] = x[i - 1] 
        y[i] = y[i - 1] - step_size 
        
    else: # y-up
        x[i] = x[i - 1]
        y[i] = y[i - 1] + step_size
        
# Plotting walk
plt.plot(x,y)
plt.axis('equal')
plt.title(f'Walk with {n} steps')
plt.xlabel('x axis')
plt.ylabel('y axis')
plt.show()
plt.close()

# First hunt - not perfect or as detailed as I want it to be, but a first experiment
m = 100 # length and width of search space
food_num = int(math.log(m)) # number of pieces of food in search space
A = np.zeros((m,m))

# Place food in search space
for i in range(1,food_num + 1):
    x_cord = random.randint(0,m-1)
    y_cord = random.randint(0,m-1)
    
    if (A[x_cord][y_cord] == 0):
        A[x_cord][y_cord] += 1 # value of 1 represents food is present
    
# Place predator in search space
pred_path = [] # list of all cells predator visits
        
x_cord = random.randint(0,m-1)
y_cord = random.randint(0,m-1)

if (A[x_cord][y_cord] == 0):
    A[x_cord][y_cord] += 2 # value of 2 represents predator is/was present 
    pred_path.append((x_cord, y_cord))
     
# Let the hunt begin
hunt_bool = True

while (hunt_bool):
    x_step = (-1)**(random.randint(1,2))*random.randint(1,int(math.log(m)))
    y_step = (-1)**(random.randint(1,2))*random.randint(1,int(math.log(m)))
    
    current_x = (pred_path[-1][0] + x_step)%(m-1) # mod wraps path
    current_y = (pred_path[-1][1] + y_step)%(m-1) #
    
    pred_path.append((current_x, current_y))
    
    if (A[current_x][current_y] == 1):
        print()
        print('- - - - - -')
        print()
        print(f'Food found in {len(pred_path) -1} steps!')
        hunt_bool = False
        
    else:
        A[current_x][current_y] += 2
