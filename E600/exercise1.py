x = 0
vowels = ['a', 'e', 'i', 'o', 'u']
s = 'azcbobobegghakl'
for l in range(len(s)):
    if s[l] in vowels:
        x = x + 1

print("Number of vowels: {}" .format(x))
