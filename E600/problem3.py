# 2. for i in range(len(list)):
#    check if list[i+1] comes after list[i]
#    if yes, add list[i] to groupA (list)
#    if no, start new groupB at list[i+1]
#    .....
# 3. compare groupA with groupB ...: return largest group 
s = 'azcbobobegghakl' # test string
g1 = []
g2 = []
g3 = []
g4 = []
g5 = []
g6 = []
i = 0
while i < len(s):
    if s[i] < s[i+1] and i < len(s):
        g1.append(s[i])
    i = i + 1
print(g1)