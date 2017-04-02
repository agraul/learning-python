# import argv from module sys to parse cli argument when launching
from sys import argv
# save first two arguments in variables
script, filename = argv
# open file from argument and save it in txt
txt = open(filename)

# print content of variable txt
print(f"Here's your file {filename}: ")
print(txt.read())

# print question, save answer in new variable
print("Type the filename again:")
file_again = input("> ")

# open file from input() and save it in txt_again
txt_again = open(file_again)

# print content of variable txt_again
print(txt_again.read())
