team1 = list(map(int,input().split()))
team2 = list(map(int,input().split()))

score1 = 0
score2 = 0
res = []
flag = False

for i in range(9):
    score1 += team1[i]
    if score1 > score2:
        res.append(True)
    elif score1 < score2:
        res.append(False)

    score2 += team2[i]
    if score1 > score2:
        res.append(True)
    elif score1 < score2:
        res.append(False)

if True in res[:-1] and res[-1] == False:
    print('Yes')
else:
    print('No')