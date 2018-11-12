#!/usr/bin/python
# Written in python 2.7
# 11/10/18
# Lu


def binary_search(list, item):

    #low and high kep track of which
    # part of the list I am searching
    low = 0
    high = len(list) -1

    # While there is not 1 element
    # remaning, keep searching
    while low <= high:

        # Check the middle element
        mid = (low + high) / 2
        guess = list[mid]

        # Found the Item
        if guess == item:
            return mid

        # If the guess was too high
        if guess > item:
            high = mid -1

        #If the guess was to low
        else:
            low = mid + 1

    #If the item (digit in second parameter) does not exist
    return None

mList = [1, 3, 5, 7, 9]

print binary_search(mList, 3) # =>1
print binary_search(mList, -1) #None
