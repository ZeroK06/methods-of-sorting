import sys
def method(arr):
    if(len(arr)>1):        
        piv=int(len(arr)/2)
        val=arr[piv]
        lft=[i for i in arr if i<val]
        mid=[i for i in arr if i==val]
        rgt=[i for i in arr if i>val]

        res=method(lft)+mid+method(rgt)
        return res
    else:
        return arr
sys.modules[__name__] = method