from makeLists import *
from sortingAlgorithms import *
from timing import time_function 
from tableInText import *

def plot_fib(n):
    'Generate a plot showing how long it took to compute the ith fibonnaci number.'
    import matplotlib.pyplot as plt

    times = []
    for i in range(n):
        t, _ =  insertionSort(reversed(i))
        times.append(t)

    plt.plot(times)
    plt.show()

plot_fib(1000)