from random import randint


def randomArr(lengthArr=10):
    arr = []
    for i in range(lengthArr):
        arr.append(randint(0, 100))
    return arr
