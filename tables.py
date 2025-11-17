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

def insertion_data(n):
    'Generate a plot showing how long it took to insertion sort a worst case n element list.'


    times = []
    for i in range(n):
        t, _ =  insertionSort(reversed(i))
        times.append(t)
    print(times)
    return times

def bubble_data(n):
    'Generate a plot showing how long it took to bubble sort a worst case n element list.'


    times = []
    for i in range(n):
        t, _ =  bubbleSort(reversed(i))
        times.append(t)

    print(times)
    return times

def merge_data(n):
    'Generate a plot showing how long it took to merge sort a worst case n element list.'

    times = []
    for i in range(n):
        t, _ =  mergeSort(reversed(i), i)
        times.append(t)

    print(times)
    return times

def table_reversed_lists(n):
    import matplotlib.pyplot as plt
    plt.title("Sorting time on reversed lists of various lengths ")
    plt.xlabel("Length of list")
    plt.ylabel("Time taken to sort")
    plt.plot(insertion_data(n), label="Insertion Sort")
    plt.plot(bubble_data(n), label = "Bubble Sort")
    plt.plot(merge_data(n), label = "Merge Sort")
    plt.legend()
    plt.show()