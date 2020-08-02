# print 1 to nth-dimension, volume constant, 
# and necessary radius for sphere to have unit volume
#
# Inspiration from Richard Hamming's
# The Art of Doing Science and Engineering, Learning to Learn

import numpy as np

Cs = [2, np.pi] # list of volume constants
k = 10 # highest dimension interested in
       # try k = 10, k = 100, and k = 500

for n in range(3,k+1): # add C_n to Cs for n >= 3
    C_nm2 = Cs[n-3]
    Cs.append((2*np.pi*C_nm2)/n)

for n in range(1,k+1): # perform and print calculation
    C_n = Cs[n-1]
    r = (1/C_n)**(1/n)
    print(f'Dimension: {n}, C_n: {Cs[n-1]:.5f} Radius for Unit Sphere: {r:.5f}')
