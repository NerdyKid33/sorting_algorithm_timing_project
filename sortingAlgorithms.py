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

def insertionSort(curList):
    n = len(curList)
    res = []
    for i in range(0, n):
        res.append(curList[i])
        curIndex = i 
        print(curIndex)
        while (curIndex>0 and curList[curIndex-1]>curList[curIndex]):
            res[curIndex], res[curIndex-1] = res[curIndex-1], res[curIndex]
            curIndex-=1

    return res

print(insertionSort([3, 2, 1]))