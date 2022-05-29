#2초
from itertools import permutations
t = int(input())
for i in range(t):
    n = int(input())
    data = list(map(int,input().split()))

    temp = list(permutations(range(n), 2))
    res = 0
    for x,y in temp:
        res += (data[x] % data[y])
    print('#'+ str(i+1), end=' ')
    print(res)





