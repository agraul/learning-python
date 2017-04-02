#!/usr/bin/python3
# how to measure the time it takes a python program to execute.

import time


def calcProd():
    # Calculate the product of the first 100.000 numbers.
    product = 1
    for i in range(1, 100000):
        product *= i
    return product

startTime = time.time()
prod = calcProd()
endTime = time.time()

print('The result is {} digits long.' .format(len(str(prod))))
print('It took {} seconds to calculate.' .format(endTime - startTime))
