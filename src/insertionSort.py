
import sys


def method(arr):
    for step in range(1, len(arr)):
        key = arr[step]
        j = step - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j = j - 1

        arr[j + 1] = key
    return arr


sys.modules[__name__] = method
