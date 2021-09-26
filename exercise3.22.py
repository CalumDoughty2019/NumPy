import sys
import numpy as np

d = 10

simple_array = np.array([
    d
], dtype='uint8')

d = d + 10
while d <= 255:
    simple_array = np.append(simple_array, d)
    d = d + 10
print(simple_array)
print()
#sys.exit(0)

multi = 0
cutoff = 100
#while i in simple_array < cutoff:
new_array = []
for a in simple_array:
    if a < cutoff:
        while a < cutoff:
            multi = a * 2
            a = a*2
        new_array.append(multi)
    else:
        new_array.append(a)
simple_array = np.array(new_array)
print(simple_array)
print()
#sys.exit(0)

new_array = []
for a in simple_array:
    if a > 150 and a <200:
        new_array.append(a)
simple_array = np.array(new_array)
print(simple_array)
print()