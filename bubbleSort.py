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



print(bubbleSort([6, 5, 4, 3]))