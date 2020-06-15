# Quadratic Forms

import ast
import numpy as np
from scipy import linalg
import sys
import matplotlib.pyplot as plt
import random

# For superscript T
superscript_map = {
    "0": "⁰", "1": "¹", "2": "²", "3": "³", "4": "⁴", "5": "⁵", "6": "⁶",
    "7": "⁷", "8": "⁸", "9": "⁹", "a": "ᵃ", "b": "ᵇ", "c": "ᶜ", "d": "ᵈ",
    "e": "ᵉ", "f": "ᶠ", "g": "ᵍ", "h": "ʰ", "i": "ᶦ", "j": "ʲ", "k": "ᵏ",
    "l": "ˡ", "m": "ᵐ", "n": "ⁿ", "o": "ᵒ", "p": "ᵖ", "q": "۹", "r": "ʳ",
    "s": "ˢ", "t": "ᵗ", "u": "ᵘ", "v": "ᵛ", "w": "ʷ", "x": "ˣ", "y": "ʸ",
    "z": "ᶻ", "A": "ᴬ", "B": "ᴮ", "C": "ᶜ", "D": "ᴰ", "E": "ᴱ", "F": "ᶠ",
    "G": "ᴳ", "H": "ᴴ", "I": "ᴵ", "J": "ᴶ", "K": "ᴷ", "L": "ᴸ", "M": "ᴹ",
    "N": "ᴺ", "O": "ᴼ", "P": "ᴾ", "Q": "Q", "R": "ᴿ", "S": "ˢ", "T": "ᵀ",
    "U": "ᵁ", "V": "ⱽ", "W": "ᵂ", "X": "ˣ", "Y": "ʸ", "Z": "ᶻ", "+": "⁺",
    "-": "⁻", "=": "⁼", "(": "⁽", ")": "⁾"}

trans = str.maketrans(
    ''.join(superscript_map.keys()),
    ''.join(superscript_map.values()))

def matrix_definitness(A):
    """takes a 2D numpy array A, and outputs if it is PD, SPD, ND, SND or ID"""
    
    U, s , Vh = linalg.svd(A)
    
    if (np.all(s > 0)):
        return 'Positive Definite'
    
    elif (np.all(s >= 0)):
        return 'Semi-Positive Definite'
    
    elif (np.all(s < 0)):
        return 'Negative Definite'
    
    elif (np.all(s <= 0)):
        return 'Semi-Negative Definite'
    
    else:
        return 'Indefinite'

# Get matrix from input
Mstr = input('Enter (2x2) Matrix of Quadratic Form: ')
Mlist = ast.literal_eval(Mstr)
A = np.array(Mlist)

# Error Messages
if (A.shape[0] != A.shape[1]):
    print('ERROR - Matrix is not square.')
    sys.exit()
    
elif (not np.all(A - A.transpose() == 0)):
    print('ERROR - 02 - Matrix is not symetric.')
    sys.exit()
    
elif (A.shape[0] != 2 or A.shape[1] != 2):
    print('ERROR - 03 - Matrix is not (2x2)')
    sys.exit()

# Get eigenvalues and vectors
S, U = linalg.eig(A)

# Print definitness of matrix
print()
print('Matrix is ' + matrix_definitness(A))

# Get Constant from input
c_ = int(input('Enter Constant: '))

# Plotting
lam1 = S[1].real
lam2 = S[0].real

a_ = A[0][0]
b_ = A[0][1]
k_ = A[1][0]
d_ = A[1][1]

super_T = 'T'.translate(trans)

x = np.linspace(-(np.sqrt(c_ + np.sqrt(c_))), np.sqrt(c_ + np.sqrt(c_)), 1000)
y = np.linspace(-(np.sqrt(c_ + np.sqrt(c_))), np.sqrt(c_ + np.sqrt(c_)), 1000)
X, Y = np.meshgrid(x,y)

# Graph Non-Standard Position
plt.subplot(1,3,1)
F = a_*(X**2) + b_*(X*Y) + k_*(X*Y) + d_*(Y**2) - c_
plt.contour(X,Y,F,[0],colors='red')
plt.gca().set_aspect('equal')
plt.xlabel('x_1')
plt.ylabel('x_2')
plt.title(f'x{super_T}Ax = {c_}, \nNon-Standard Position')

# Graph Standard Position
plt.subplot(1,3,2)
G = lam1*(X**2) + lam2*(Y**2) - c_
plt.contour(X,Y,G,[0],colors='blue')
plt.gca().set_aspect('equal')
plt.xlabel('x_1')
plt.ylabel('x_2')
plt.title(f'x{super_T}Ax = {c_}, \nStandard Position')

# Graph both positions
plt.subplot(1,3,3)
plt.contour(X,Y,F,[0],colors='red')
plt.contour(X,Y,G,[0],colors='blue')
plt.gca().set_aspect('equal')
plt.xlabel('x_1')
plt.ylabel('x_2')
plt.title(f'x{super_T}Ax = {c_}, \nBoth Positions')

plt.tight_layout()
plt.show()
plt.close()
plt.savefig('quad' + str(random.randint(10,100)) + '.pdf')

# Try
# [[5,-2],[-2,5]], c = 48
# [[1,-4],[-4,-5]], c = 16
