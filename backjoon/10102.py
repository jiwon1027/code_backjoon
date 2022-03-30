V = int(input())
data = input()
cntA = 0
cntB = 0

for i in data:
    if i == 'A':
        cntA += 1
    else:
        cntB += 1

if cntA > cntB:
    print('A')
elif cntA < cntB:
    print('B')
else:
    print('Tie')
