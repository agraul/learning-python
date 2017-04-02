#!/usr/bin/python3

end = int(input("How many numbers of the fibonacci sequence would you like to see?\n"))
f_sequence = [0, 1]
for i in range(2, end, 1):
    f_temp = f_sequence[i-2] + f_sequence[i-1]
    f_sequence.append(f_temp)
print(f_sequence)
