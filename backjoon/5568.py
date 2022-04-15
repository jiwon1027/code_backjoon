n = int(input())
k = int(input())
card = []
for _ in range(n):
    card.append(int(input()))

res = set()
from itertools import permutations
for i in permutations(card,k):
    temp = ''
    for j in range(len(i)):
        temp += str(i[j])
    res.add(temp)
print(len(res))
