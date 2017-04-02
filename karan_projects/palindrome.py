#!/usr/bin/python3
# Check if a word is a palindrome.
s = input("Please enter a word: ")
if s == s[::-1]:
    print("{} is a palindrom: {}".format(s, s[::-1]))
else:
    print("{} is not a palindrom: {}".format(s, s[::-1]))
