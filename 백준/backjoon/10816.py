#Hash map

import sys
input = sys.stdin.readline

n = int(input())
data1 = list(map(int,input().split()))

m = int(input())
data2 = list(map(int,input().split()))

hash = {}

for i in data1:
    print(hash)
    if i in hash:
        hash[i] += 1
    else:
        hash[i] = 1

for i in data2:
    if i in hash:
        print(hash[i], end=' ')
    else:
        print(0, end=' ')