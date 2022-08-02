n = int(input())
data = list(map(int,input().split()))

from itertools import permutations
per = permutations(data)
res = 0

for i in per:
    #print(i)
    temp = 0
    for j in range(len(i)-1):
        #print(j)
        temp += abs(i[j] - i[j+1])
    if temp > res:
        res = temp
print(res)



