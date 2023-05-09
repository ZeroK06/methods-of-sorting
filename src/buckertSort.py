import sys
# closificacion por conteo
def method(arr):
    result = []
    count = []
    for i in range(max(arr) + 1):
        count.append(0)
    for i in range(len(arr)):
        count[arr[i]] += 1
    #llenar resultados
    for i in range(len(count)):
        for j in range(count[i]):
            result.append(i)

    return result

sys.modules[__name__] = method