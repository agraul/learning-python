#/usr/bin/python3

# If a word starts with a consonant, move it to the back and add -ay
vowels = ['a', 'e', 'i', 'o', 'u']
l = ["There", "are", "some", "words", "to", "use", "this", "programm", "on."]
l_new = []
print(l)
i = 0
while i < len(l):
    word = l[i]
    if word[0] not in vowels:
        word = word[1:] + word[0] + "ay"
        l[i] = word
        i += 1
print(l)
