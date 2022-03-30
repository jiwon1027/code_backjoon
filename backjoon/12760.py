N, M = list(map(int,input().split()))

score = [0] * N
card = []

for _ in range(N):
    card.append(sorted(list(map(int,input().split())),reverse = True))

for i in range(M):
    temp = []
    for j in range(N):
        temp.append(card[j][i])
    max_value = max(temp)
    for j in range(N):
        if max_value == temp[j]:
            score[j] += 1
res = max(score)
for i in range(N):
    if score[i] == res:
        print(i+1, end=' ')