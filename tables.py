from makeLists import *
from sortingAlgorithms import *
from timing import time_function 
import matplotlib as plt


def tableMerge(n):
    'Sort reversed lists length i from 0 to n with merge sort, as well as how long it took to calculate them.'
    print('i\t\ttime')
    for i in range(1, n):
        t, r = mergeSort(mostlySorted(i), i)
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

def insertion_data(n, x):
    'Generate a plot showing how long it took to insertion sort a worst case n element list.'
    times = []
    for i in range(1, n):
        if (x==1):
            t, _ =  insertionSort(preSorted(i))
            times.append(t)
        elif (x==2):
            t, _ =  insertionSort(mostlySorted(i))
            times.append(t)
        elif (x==3):
            t, _ =  insertionSort(randomList(i))
            times.append(t)
        elif (x==4):
            t, _ =  insertionSort(reversed(i))
            times.append(t)
    return times

def bubble_data(n, x):
    'Generate a plot showing how long it took to bubble sort a worst case n element list.'
    times = []
    for i in range(1, n):
        if (x==1):
            t, _ =  bubbleSort(preSorted(i))
            times.append(t)
        elif (x==2):
            t, _ = bubbleSort(mostlySorted(i))
            times.append(t)
        elif (x==3):
            t, _ = bubbleSort(randomList(i))
            times.append(t)
        else:
            t, _ = bubbleSort(reversed(i))
            times.append(t)

    return times

def merge_data(n, x):
    'Generate a plot showing how long it took to merge sort a worst case n element list.'

    times = []
    for i in range(1, n):
        if (x==1):
            t, _ =  mergeSort(preSorted(i), i)
            times.append(t)
        elif (x==2):
            t, _ = mergeSort(mostlySorted(i), i)
            times.append(t)
        elif (x==3):
            t, _ = mergeSort(randomList(i), i)
            times.append(t)
        else:
            t, _ = mergeSort(reversed(i), i)
            times.append(t)

    return times

def table_reversed_lists(n, x):
    import matplotlib.pyplot as plt

    if (x==1):
        plt.title("Sorting time on presorted lists of various lengths ")
    elif (x==2):
        plt.title("Sorting time on mostly sorted lists of various lengths")
    elif (x==3):
        plt.title("Sorting time on randomly distributed lists of various lengths")
    else:
        plt.title("Sorting time on reversed lists of various lengths")
    

    plt.xlabel("Length of list")
    plt.ylabel("Time taken to sort")
    plt.plot(insertion_data(n, x), label="Insertion Sort")
    plt.plot(bubble_data(n, x), label = "Bubble Sort")
    plt.plot(merge_data(n, x), label = "Merge Sort")
    plt.legend()
    plt.show()