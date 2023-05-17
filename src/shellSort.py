import sys


def method(arr):
    interval = len(arr) // 2
    while interval > 0:
        for i in range(interval, len(arr)):
            temp = arr[i]
            j = i
            while j >= interval and arr[j - interval] > temp:
                arr[j] = arr[j - interval]
                j -= interval

            arr[j] = temp
        interval //= 2
    return arr


sys.modules[__name__] = method
