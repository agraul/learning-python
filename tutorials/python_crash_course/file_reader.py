filename = 'learning_python.txt'

with open(filename) as file_object:
    for line in file_object:
        print(line.replace('Python', 'C').rstrip())

with open(filename) as file_object2:
    for line in file_object2:
        print(line.replace('Python', 'C++').rstrip())


with open(filename) as file_object3:
    lines = file_object3.readlines()

for line in lines:
    print(line.replace('Python', 'Java').rstrip())


