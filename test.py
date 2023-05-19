
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
from services import generateArrTxt
import json
import os
import datetime

colors = ["black", "blue", "brown", "cyan", "darkgray", "gray", "green", "lightgray",
          "lime", "magenta", "olive", "orange", "pink", "purple", "red", "teal", "violet", "yellow"]

#
# Generador de archivo para test
#


generateArrTxt.generateTxt()

resultMethods = json.loads(
    '[{"name": "bubbleSort","res":[] },{"name": "buckertSort","res":[] },{"name": "heapSort","res":[] },{"name": "insertSort","res":[] },{"name": "quickSort","res":[] },{"name": "selectionSort","res":[] },{"name": "shellSort","res":[] }]')
res = []
for path in os.listdir('data'):
    if os.path.isfile(os.path.join('data', path)):
        res.append(path)

print(res)


def test(*methods, numData=1):
    plots = ""
    arr = randomArr.randomArr(numData)
    result = []
    index = 0

    for i in range(len(methods)):
        currentResult = []
        firstTime = datetime.datetime.now()
        methods[i](json.loads(open('data/200_a.txt', 'r').read()))
        lastTime = datetime.datetime.now()
        currentResult.append((lastTime - firstTime).total_seconds())
        firstTime = datetime.datetime.now()
        methods[i](json.loads(open('data/400_a.txt', 'r').read()))
        lastTime = datetime.datetime.now()
        currentResult.append((lastTime - firstTime).total_seconds())
        firstTime = datetime.datetime.now()
        methods[i](json.loads(open('data/800_a.txt', 'r').read()))
        lastTime = datetime.datetime.now()
        currentResult.append((lastTime - firstTime).total_seconds())
        firstTime = datetime.datetime.now()
        methods[i](json.loads(open('data/1600_a.txt', 'r').read()))
        lastTime = datetime.datetime.now()
        currentResult.append((lastTime - firstTime).total_seconds())
        firstTime = datetime.datetime.now()
        methods[i](json.loads(open('data/3200_a.txt', 'r').read()))
        lastTime = datetime.datetime.now()
        currentResult.append((lastTime - firstTime).total_seconds())
        firstTime = datetime.datetime.now()
        methods[i](json.loads(open('data/6400_a.txt', 'r').read()))
        lastTime = datetime.datetime.now()
        currentResult.append((lastTime - firstTime).total_seconds())
        firstTime = datetime.datetime.now()
        methods[i](json.loads(open('data/12800_a.txt', 'r').read()))
        lastTime = datetime.datetime.now()
        currentResult.append((lastTime - firstTime).total_seconds())
        firstTime = datetime.datetime.now()
        methods[i](json.loads(open('data/25600_a.txt', 'r').read()))
        lastTime = datetime.datetime.now()
        currentResult.append((lastTime - firstTime).total_seconds())
        firstTime = datetime.datetime.now()
        methods[i](json.loads(open('data/51200_a.txt', 'r').read()))
        lastTime = datetime.datetime.now()
        currentResult.append((lastTime - firstTime).total_seconds())
        firstTime = datetime.datetime.now()
        methods[i](json.loads(open('data/102400_a.txt', 'r').read()))
        lastTime = datetime.datetime.now()
        currentResult.append((lastTime - firstTime).total_seconds())

        print(resultMethods[index]["name"])
        coordinates = ''
        for i in range(len(currentResult)):
            coordinates = coordinates + \
                '({},{})'.format(2**(i+1)*100, currentResult[i])
        plot = "\\addplot[color="+colors[randint(0, len(colors)-1)]+",mark=square] \n coordinates {" + \
            coordinates + "}; \n \\addlegendentry{" + \
            resultMethods[index]["name"] + "}\n"
        plots = plots+plot
        index = index+1
    response = open('plots.txt', 'w')
    response.write(plots)
    return result


print(test(bubbleSort, buckertSort, heapSort, insertionSort, quickSort, selectionSort,
      shellSort, numData=500))
