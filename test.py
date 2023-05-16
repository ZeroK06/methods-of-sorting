
from src import buckertSort
from src import insertionSort
from src import selectionSort
from src import bubbleSort
from src import quickSort
from src import heapSort
from services import randomArr
from time import time
from random import randint
import json
import os
#
# Generador de archivo para test
#


def generateTxt():
    for i in range(5):
        currentFile = open('data/{}_a.txt'.format(2**(i+1)*100), 'w')
        currentArr = randomArr.randomArr(2**(i+1)*100)
        currentFile.write(json.dumps(currentArr))
        currentFile.close()
    return 0


generateTxt()

resultMethods = json.loads(
    '[{"name": "bubbleSort","res":[] },{"name": "buckertSort","res":[] },{"name": "heapSort","res":[] },{"name": "insertSort","res":[] },{"name": "quickSort","res":[] },{"name": "selectionSort","res":[] },{"name": "shellSort","res":[] }]')
res = []
for path in os.listdir('data'):
    if os.path.isfile(os.path.join('data', path)):
        res.append(path)

print(res)


def test(*methods, numData=1):

    arr = randomArr.randomArr(numData)
    result = []
    index = 0

    for i in range(len(methods)):
        currentResult = []
        prom = 0
        print(resultMethods[index]["name"])
        for path in os.listdir('data'):
            if os.path.isfile(os.path.join('data', path)):
                currentArr = json.loads(open('data/'+path, 'r').read())
                print(path)
                firstTime = time()
                res = methods[i](currentArr)
                lastTime = time()
                currentFile = open('data/'+path, 'w')
                currentFile.write(str(res))
                currentFile.close()
                prom += lastTime - firstTime
                currentResult.append(prom)

        print(currentResult)
        index = index+1
    return result


print(test(buckertSort, insertionSort, selectionSort,
      bubbleSort, quickSort, heapSort, numData=500))
