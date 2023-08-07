#!/usr/bin/python

#binary search algorithm

ml = lst(range(1, 5))
item = 2

low = 0
high = len(ml) - 1
count = 0
while low <= high:
    mid = (low + high)//2
    guess = ml[mid]
    if guess == item:
        print("Found")
        break
    if guess > item:
        high = mid - 1
    else:
        low = mid + 1
    count += 1
print(count)

