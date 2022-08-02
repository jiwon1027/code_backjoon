import sys
from itertools import combinations

n = int(sys.stdin.readline())

data = list()
for i in range(1, 11):
    for comb in combinations(range(0, 10), i):
        comb = list(comb)
        comb.sort(reverse=True)
        data.append(int("".join(map(str, comb))))

data.sort()

try:
    print(data[n])
except:
    print(-1)