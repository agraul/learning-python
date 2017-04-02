#!/usr/bin/env python3
low = 0
high = 100
ans = (low + high) // 2

while True:
    print("Is your secret number {}?" .format(ans))
    res =  input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")

    if res == 'h':
        high = ans
    elif res == 'l':
        low = ans
    elif res == 'c':
        print("Game over. Your secret number was {}" .format(ans))
        break
    elif input != 'l' or 'h' or 'c':
        print("Sorry, I did not understand that input!")
    ans = (low + high) // 2
