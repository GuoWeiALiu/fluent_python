from array import array
from random import random

floats = array('d', (random() for i in range(10 ** 7)))
print(floats[-1])
memv = memoryview(floats)
print(memv.tolist())

with open('filename1.txt', 'a') as file:
    floats = str(memv.tolist())
    file.write(floats)
