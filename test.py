
from src import buckertSort
from src import insertionSort
from src import selectionSort
from src import bubbleSort
from src import quickSort
from src import heapSort
from src import shellSort
from services import randomArr
from time import time
from random import randint
import json
import os
import datetime
#
# Generador de archivo para test
#


def generateTxt():
    for i in range(10):
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
        firstTime = datetime.datetime.now()
        methods[i](json.loads(open('data/200_a.txt', 'r').read()))
        lastTime = datetime.datetime.now()
        currentResult.append((lastTime - firstTime).total_seconds() * 1000)
        firstTime = datetime.datetime.now()
        methods[i](json.loads(open('data/400_a.txt', 'r').read()))
        lastTime = datetime.datetime.now()
        currentResult.append((lastTime - firstTime).total_seconds() * 1000)
        firstTime = datetime.datetime.now()
        methods[i](json.loads(open('data/800_a.txt', 'r').read()))
        lastTime = datetime.datetime.now()
        currentResult.append((lastTime - firstTime).total_seconds() * 1000)
        firstTime = datetime.datetime.now()
        methods[i](json.loads(open('data/1600_a.txt', 'r').read()))
        lastTime = datetime.datetime.now()
        currentResult.append((lastTime - firstTime).total_seconds() * 1000)
        firstTime = datetime.datetime.now()
        methods[i](json.loads(open('data/3200_a.txt', 'r').read()))
        lastTime = datetime.datetime.now()
        currentResult.append((lastTime - firstTime).total_seconds() * 1000)
        firstTime = datetime.datetime.now()
        methods[i](json.loads(open('data/6400_a.txt', 'r').read()))
        lastTime = datetime.datetime.now()
        currentResult.append((lastTime - firstTime).total_seconds() * 1000)
        firstTime = datetime.datetime.now()
        methods[i](json.loads(open('data/12800_a.txt', 'r').read()))
        lastTime = datetime.datetime.now()
        currentResult.append((lastTime - firstTime).total_seconds() * 1000)
        firstTime = datetime.datetime.now()
        methods[i](json.loads(open('data/25600_a.txt', 'r').read()))
        lastTime = datetime.datetime.now()
        currentResult.append((lastTime - firstTime).total_seconds() * 1000)
        firstTime = datetime.datetime.now()
        methods[i](json.loads(open('data/51200_a.txt', 'r').read()))
        lastTime = datetime.datetime.now()
        currentResult.append((lastTime - firstTime).total_seconds() * 1000)
        firstTime = datetime.datetime.now()
        methods[i](json.loads(open('data/102400_a.txt', 'r').read()))
        lastTime = datetime.datetime.now()
        currentResult.append((lastTime - firstTime).total_seconds() * 1000)

        print(resultMethods[index]["name"])
        print(currentResult)
        index = index+1
    return result


print(test(bubbleSort, buckertSort, heapSort, insertionSort, quickSort, selectionSort,
      shellSort, numData=500))
