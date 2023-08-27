#!/usr/bin/python

import time

def bubble_sort(mlist):
    n = len(mlist)

    for i in range(n):
        for j in range(0, n - 1 - i):
            if mlist[j] > mlist[j + 1]:
                mlist[j], mlist[j + 1] = mlist[j + 1], mlist[j]
    return mlist


def quick_sort(mlist):
    if len(mlist) < 2:
        return mlist
    else:
        pivot = mlist[0]
        less = [i for i in mlist[1:] if i <= pivot]
        greater = [i for i in mlist[1:] if i > pivot]

        return quick_sort(less) + [pivot] + quick_sort(greater)


def main():
    mstr = input("Enter a sentence: ")
    ml = list(mstr)
    
    #Find the duration of bubble sort
    start = time.time()
    print("Bubble sort: ", bubble_sort(ml))
    end = time.time()
    print("Duration of bubble sort: ", end - start)
    
    #Find the duration of quick sort
    start = time.time()
    print("Quick sort: ", quick_sort(ml))
    end = time.time()
    print("Duration of quick sort: ", end - start)
    
main()
