def burbuja(arr1):
    for i in range(len(arr1)):
        for j in range(len(arr1) - 1):
            if(arr1[j] > arr1[j + 1]):
                aux =  arr1[j]
                arr1[j] = arr1[j + 1]
                arr1[j + 1] = aux
    return arr1;
