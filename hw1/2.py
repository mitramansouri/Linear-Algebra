# define A = [[3,5,1],[-1,2,4],[2,1,3]] and B = [[2,4,-1],[3,9,0],[-2,1,4]]
# x barT = [1,2,2] ,y barT = [3,2,1]
# using numpy

from audioop import add
from re import A
from numpy import linalg as LA
import numpy as np 
# defining 

# A
matrix_a = np.array([[3,5,1],
                    [-1,2,4],
                    [2,1,3]])

# B
matrix_b = np.array([[2,4,-1],
                    [3,9,0],
                    [-2,1,4]])

# X - vertical
x = np.array([[1],
		[2],
		[2]])

# Y - vertical
y = np.array([[3],
		[2],
		[1]])

# Calculating 
# x+y
addition = x + y
print(f"addition is {addition}")

# -3x+2y
scalar_mult = -3*x  + 2*y
print(f"scalar_mult is {scalar_mult}")

# ||x||
norm_x = LA.norm(x)
print(f"norm_x is {norm_x}")

# rms(X) using ||x||
root_mean_square_x = np.sqrt(np.mean(x**2))
print(f"rms is {root_mean_square_x}")

# std(x)
std_x = np.std(x)
print(f"std is {std_x}")

# A.B
dot_product = np.dot(matrix_a, matrix_b)
print(f"dot product of A and B is {dot_product}")

# Ax
Ax = np.dot(matrix_a, x)
print(f"AX is {Ax}")

# AT
transpose_A = np.transpose(matrix_a)
print(f"Transpose of A is {transpose_A}")