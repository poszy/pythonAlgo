#!/usr/bin/python


def findSmallestIndex(arr):

  smallest = arr[0] # Store the smallest value
  smallest_index=0 # store the index of the smallest value


  for i in range(1, len(arr)):

    if arr[i] < smallest:
      smallest = arr[i]
      smallest_index = i

  return smallest_index



def selectionSort(arr):
  #Initialize blank array
  newArr= []

  # loop through the length of the list taken as a parameter

  for i in range(len(arr)):
    # find the smallest index of the list taken as a parameter
    smallest = findSmallestIndex(arr)

    # Remove and return the smallets index of the list taken as a parameter
    # Pop removes and returns last object or obj from the list, in this case we
    # are giving it the parameter 'smallest' so remove that and return and append it to the newArr
    newArr.append(arr.pop(smallest))

    #Keep doing this until there is not anymore indexes

  return newArr


#a = [1,3,5,6,9]
#print findSmallestIndex(a)
print selectionSort([5, 3, 6, 2, 10])
