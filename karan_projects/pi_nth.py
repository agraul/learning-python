# Find PI to the Nth Digit - Enter a number and have the program generate PI up to that many decimal places. Keep a limit to how far the program will go.
import math

N = input("Please select the number of decimal places of PI you would like to see: ")
if int(N) <= 15:
    print("This is PI to {1}th digit: {0:.{1}f}".format(math.pi, N))
else:
    print("Sorry, rounding after the 15th digit gets too big. PI to 15th digit: {:.15f}" .format(math.pi))
