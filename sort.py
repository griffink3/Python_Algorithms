#!/usr/bin/python
import random

class InvalidInputException(Exception):
    def __init__(self,value):
        self.value = value
    def __str__(self):
        return repr(self.value)


def merge_sort(array):
    """merge_sort: int array -> int array
        Purpose: Sort the input array of integers in descending order using the merge sort algorithm
        Example: merge_sort([4,5,1,3,2]) -> [5,4,3,2,1]
        Throws: InvalidInputException if list is None
    """
    if array == None:
        raise InvalidInputException(array)
    n = len(array)
    if n <= 1:
        return array
    mid = n//2
    left = merge_sort(array[:mid])
    right = merge_sort(array[mid:])
    return merge(left, right)

def merge(left, right):
    """
    Input: Two arrays to be merged in sorted order
    Output: An array that is the two input arrays merged together in sorted order
    Purpose: A helper method for mergesort that merges two lists
    """
    sortedArray = []
    leftIndex = 0
    rightIndex = 0
    while leftIndex < len(left) and rightIndex < len(right):
        if left[leftIndex] >= right[rightIndex]:
            sortedArray.append(left[leftIndex])
            leftIndex += 1
        else:
            sortedArray.append(right[rightIndex])
            rightIndex += 1
    if leftIndex < len(left):
        sortedArray = sortedArray + left[leftIndex:]
    if rightIndex < len(right):
        sortedArray = sortedArray + right[rightIndex:]
    return sortedArray

def quick_sort(array):
    """quick_sort: int array -> int array
        Purpose: Sort the input array of integers in descending order using the quicksort algorithm
        Example: quick_sort([4,5,1,3,2]) -> [5,4,3,2,1]
        Throws: InvalidInputException if list is None
    """
    if array == None:
        raise InvalidInputException(array)
    if len(array) <= 1:
        return array
    pivot = array[random.randint(0,len(array)-1)]
    less = []
    equal = []
    greater = []
    for number in array:
        if number < pivot:
            less.append(number)
        elif number > pivot:
            greater.append(number)
        else:
            equal.append(number)
    return quick_sort(greater) + equal + quick_sort(less)

def radix_sort(array):
    """radix_sort: int array -> int array
        Purpose: Sort the input array of integers in descending order using the radixsort algorithm
        Example: radix_sort([4,5,1,3,2]) -> [5,4,3,2,1]
        Throws: InvalidInputException if list is None
    """
    if array == None:
        raise InvalidInputException(array)
    sortedArray = []
    posNum = []
    negNum = []
    mostDigits = 0
    for number in array:
        num = str(abs(number)) # We don't want the negative signs to be in the strings
        if len(num) > mostDigits:
            mostDigits = len(num) # Storing the greatest number of digits
        if number >= 0:
            posNum.append(num)
        else:
            negNum.append(num)
    posNum = help_radix_sort(posNum, mostDigits, 10)
    for number in posNum:
        num = int(number)
        sortedArray.append(num)
    negNum = help_radix_sort(negNum, mostDigits, 0)
    for number in negNum:
        num = -int(number)
        sortedArray.append(num)
    return sortedArray

def help_radix_sort(array, mostDigits, index):
    """
    Input: An array of ints in string form, an int representing the greatest
    number of digits of any number in the original set of numbers to be sorted,
    and an index that depends on whether we're sorting originally positive or
    negative numbers
    Output: An array of ints in string form in descending order if they original
    numbers were positive and ascending order if the original numbers were negative
    Purpose: A helper method for radixsort that allows us to sort both numbers that
    were both originally negative or originally positive
    """
    buckets = [[] for x in range(11)]
    for i in range(0, mostDigits):
        for number in array:
            if len(number) < i+1:
                buckets[index].append(number)
            else:
                # The number at the front isn't necessarily the ones digit
                buckets[index-int(number[len(number)-1-i])-1].append(number)
        array = []
        for list in buckets:
            array = array + list
        buckets = [[] for x in range(11)]
    return array
