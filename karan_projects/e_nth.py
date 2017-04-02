# Find e to the Nth Digit - Enter a number and have the program generate e up to that many decimal places. Keep a limit to how far the program will go.
import math

N = input("Please select the number of decimal places of e you would like to see: ")
if int(N) <= 15:
    print("This is e to {1}th digit: {0:.{1}f}".format(math.e,N))
else:
    print("Sorry, rounding after the 15th digit gets too big. e to 15th digit: {:.15f}" .format(math.e))
