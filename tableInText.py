from makeLists import *
from sortingAlgorithms import *
from timing import time_function 


def tableMerge(n):
    'Sort reversed lists length i from 0 to n with merge sort, as well as how long it took to calculate them.'
    print('i\t\ttime')
    for i in range(1, n):
        t, r = mergeSort(reversed(i), i)
        print(f'{i}\t\t{t}')

def tableInsertion(n):
    'Sort reversed lists length i from 0 to n with insertion sort, as well as how long it took to calculate them.'
    print('i\t\ttime')
    for i in range(1, n):
        t, r = insertionSort(mostlySorted(i))
        print(f'{i}\t\t{t}')

def tableBubble(n):
    'Sort reversed lists length i from 0 to n with buble sort, as well as how long it took to calculate them.'
    print('i\t\ttime')
    for i in range(1, n):
        t, r = bubbleSort(mostlySorted(i))
        print(f'{i}\t\t{t}')