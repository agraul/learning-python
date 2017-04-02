#!/usr/bin/python3

def mergeSort(numbers):
    """
    Recursively divides list of numbers in smaller lists until len(list) == 1
    """
    A = numbers  # Set A to the list we pass as argument to mergeSort
    sizeA = len(A)
    if sizeA == 1:
        return A  # end recursivity
    Al = A[:sizeA/2]  # left part of A
    Ar = A[sizeA/2:]  # right part of A
    Al = mergeSort(Al) # pass left part to mergeSort for further division
    Ar = mergeSort(Ar)  # pass right part to mergeSort for further division
    return merge(Al, Ar) # pass both sided to merge

def merge(a, b):
    """ Merge two lists in increasing order"""
    c = []  # list to store result in
    while a and b:  # compare a to b and put smaller number into c
        if a[0] > b[0]:
            c.append(b[0])
            b = b[1:]
        else:
            c.append(a[0])
            a = a[1:]
    while a:  # if only a has a number, add it to c
        c.append(a[0])
        a = a[1:]
    while b:  # if only b has a number, add it to c
        c.append(b[0])
        b = b[1:]
    return c # return sorted list

A = []
print("Please enter 10 numbers: ")
for i in range(10):
    A.append(int(input()))
print(mergeSort(A))
