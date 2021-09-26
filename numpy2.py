import sys
import numpy as np

c = np.array([2, 3, 8])
#shape
print(c.shape) #shape tells us how many dimensions are in that array
print()
#sys.exit(0)

#2d
two_d_array = np.array([
    [2, 3, 8],
    [4, 5, 6],
])
print(two_d_array)
print(two_d_array.shape) #ANS (2, 3). This means we have two lists (rows), each of which has three elements (columns)
print()
#sys.exit(0)

#slicing
c = np.array([2, 3, 8])
print(c[2])
print(c[1:])
#print()
print(two_d_array[1]) #get first object in the list (which is another list)
print(two_d_array[1][2]) #go into the first object in this list (which is anther list), and get the value at second index
print(two_d_array[1, 2]) #*SAME AS ABOVE* go into the first object in this list (which is anther list), and get the value at second index
print()
#sys.exit(0)

#find a column
print(two_d_array[:, 1]) #ignores any specific row, but takes everything from column one (of both rows)
print()
#sys.exit(0)

#masking
a = np.array([230, 10, 284, 39, 76])
cutoff = 200
print(a > cutoff) #[ True False  True False False]