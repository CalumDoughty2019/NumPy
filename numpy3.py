import sys
import numpy as np

two_d_array = np.array([
    [2, 3, 8],
    [4, 5, 6],
])

print("Original array:\n", two_d_array)
#elementwise multiplication
two_d_array[:, 1] = two_d_array[:, 1] * 3 #multiply 2nd columns by 3
print("Transformed array:\n", two_d_array)
print()
#sys.exit(0)

#matrix multiplication
single_vector = np.array([2, 3, 8])
transform = (np.dot(two_d_array, single_vector)) #dot product is each index mutliplied by its relative index then added together.
print("We can do matrix multiplication!")
print("This time we have multiplied:\n", two_d_array)
print("by\n", single_vector)
print("Result:\n", transform) #[ 95 101]
#done by [ 2  9  8] relative multiplied by [2 3 8]. SO 2*2=4, 9*3=27, 8*8=64. THEN 4+27+64=95
#done by [ 4 15  6] relative multiplied by [2 3 8]. SO 4*2=8, 15*3=45, 6*8=48. THEN 8+45+48=101
