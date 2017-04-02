#! python3
#
#Fizz Buzz - Write a program that prints the numbers from 1 to 100. But for multiples of three print “Fizz” instead of the number and for the multiples of five print “Buzz”. For numbers which are multiples of both three and five print “FizzBuzz”.

# Main loop that prints numbers
n = 1
while n <= 100:
    m = n

# Exception for n % 5 == 0 and n % 3 == 0
    if n % 5 == 0 and n % 3 == 0:
        m = "FizzBuzz"

# Exception for n % 3 == 0
    elif n % 5 == 0:
        m = "Buzz"

# Exception for n % 5 == 0
    elif n % 3 == 0:
        m = "Fizz"

    print(m)
    n = n+1

