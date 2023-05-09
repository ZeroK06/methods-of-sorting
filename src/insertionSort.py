
import sys
def method(arr):
    for i in range(1 ,len(arr) - 1):
        if arr[i - 1] > arr[i]:
            aux = arr[i - 1]
            arr[i - 1] = arr[i]
            arr[i] = aux 
    return arr


sys.modules[__name__] = method