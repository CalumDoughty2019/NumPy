import sys
import numpy as np

#using numpy
c = np.array([2, 3, 8])
print(c)
print(type(c))
#sys.exit(0)

d = np.array(["Hi", 6])
print(d)
print(type(d))
#sys.exit(0)

#elementwise addition & subtraction
print("Elementwise Addition: add 2", c + 2)
print("Elementwise Subtraction: subtract 2", c - 2)
#elementwise multiplication & division
print("Elementwise Multiplication: multiply by 2", c * 2)
print("Elementwise Division: divide by 2", c / 2)
#elementwise exponent
print("Elementwise Exponent: power of 2", c ** 2)
#sys.exit(0)

#THESE WONT WORK, as d has a string value
#print("Elementwise Addition: add 2", d + 2)
#print("Elementwise Subtraction: subtract 2", d - 2)

#vector(scalar) multiplication (dot product)
# c=np.array([2, 3, 8]) - for easy comparison
h = np.array([2, 5, 1])
print("Scalar Multiplication", np.dot(c, h))