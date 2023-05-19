from services import randomArr
import json


def generateTxt():
    for i in range(10):
        currentFile = open('data/{}_a.txt'.format(2**(i+1)*100), 'w')
        currentArr = randomArr.randomArr(2**(i+1)*100)
        currentFile.write(json.dumps(currentArr))
        currentFile.close()
    return 0
