
from src import buckertSort
from src import insertionSort
from src import selectionSort
from src import bubbleSort
from src import quickSort
from src import heapSort
from services import randomArr
from time import time
from random import randint


def test(*methods, numData=1):
    arr = randomArr.randomArr(numData)
    result = []
    for i in range(len(methods)):
        prom = 0
        for j in range(len(arr)):
            firstTime = time()
            methods[i](arr)
            lastTime = time()
            prom += lastTime - firstTime
        result.append(prom / len(arr))

    return result


print(test(buckertSort, insertionSort, selectionSort,
      bubbleSort, quickSort, heapSort, numData=500))
