from burbuja import method
from time import time 
from random import randint

arr = []
numGenerate = int(input("len: "))

for i in range(numGenerate):
    arr.append(randint(0,9))
#print(arr)
firstTime = time()
method.burbuja(arr)
#print(method.burbuja(arr))
lastTime = time()
print(lastTime - firstTime)

