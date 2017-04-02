#!/usr/bin/env python3
x = 0
s = 'uovxobbobbobo'
y = range(len(s))
for l in y:
    if s[l] == 'b' and l < y[-1]:
        if s[l+1] == 'o' and l+1 < y[-1]:
            if s[l+2] == 'b':
                x = x + 1
print("Number of times bob occurs is: {}" .format(x))

