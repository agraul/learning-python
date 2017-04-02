filename = 'guests.txt'

with open(filename, 'a') as file_object:
    file_object.write(input("Please write your full name down: ") + "\n")
