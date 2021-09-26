import sys
#import cv2
import numpy as np

tardis = np.zeros((2, 3, 4), dtype=np.int16)
print(tardis.shape)
print(tardis)
print()
#sys.exit(0)

lots_of_numbers = np.arange(500) #not arrange, a range (of values)
print(lots_of_numbers.shape)
print(lots_of_numbers)
print()
#sys.exit(0)

a = np.zeros((100, 100, 3))
a[:, :, 0] = 255
print(a.shape)
b = np.zeros((100, 100, 3))
b[:, :, 1] = 255
c = np.zeros((100, 200, 3))
c[:, :, 2] = 255
img = c
#img = np.vstack((c, np.hstack((a, b)))) #verticalStack #horizontalStack
#cv2.imashow("Jimmy's Image", img)
#cv2.waitKey(0)