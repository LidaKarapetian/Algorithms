#!/usr/bin/python
 
#Implementation of Bubble Sort

def bubble_sort(ls):
    n = len(ls)
    for i in range(n - 1):
        for j in range(n - 1 - i):
    # Swap if the element found is greater than the next element
            if ls[j] > ls[j + 1]:          
                ls[j], ls[j + 1] = ls[j + 1], ls[j]
    return ls


#Implementation of Selected Sort

#Function returns the index of the smallest element
def SmallestIndex(arr):
    smallest = arr[0]   #To store the smallest value
    sm_ind = 0     #To store the index of the smallest value
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            sm_ind = i
    return sm_ind

#Function returns a array with sorted elements
def Sorting(arr):
    newArr = []
    for i in range(len(arr)):
        smallest = SmallestIndex(arr)
        newArr.append(arr.pop(smallest))
    return newArr

#Implementation of Quick Sort

def quicksort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        less = [i for i in array[1:] if i <= pivot]
        greater = [i for i in array[1:] if i > pivot]

        return quicksort(less) + [pivot] + quicksort(greater)

















