from timing import time_function

@time_function
def bubbleSort(curList):
    n = len(curList)
    while True:
        k = True
        for i in range(0, n-1):
            if curList[i] > curList[i+1]:
                curList[i], curList[i+1] = curList[i+1], curList[i]
                k = False
        if k:
            break


    return curList

@time_function
def insertionSort(curList):
    n = len(curList)
    res = []
    for i in range(0, n):
        res.append(curList[i])
        curIndex = i 
        while (curIndex>0 and res[curIndex-1]>res[curIndex]):
            res[curIndex], res[curIndex-1] = res[curIndex-1], res[curIndex]
            curIndex-=1

    return res

def merge(arr1, arr2, n, m):
    i = 0 
    j = 0 
    res = []
    while (i<n and j<m):
        if (arr1[i]<arr2[j]):
            res.append(arr1[i])
            i+=1
        else:
            res.append(arr2[j])
            j+=1 

    for q in range(i, n):
        res.append(arr1[q])

    for q in range(j, m):
        res.append(arr2[q])

    return res

@time_function
def mergeSort(arr, n):
    if (n<=1):
        return arr 
    
    _, x1 = mergeSort(arr[:n//2], n//2)
    _, x2 = mergeSort(arr[n//2:], n - n//2)

    return merge(x1, x2, n//2, n-n//2)
