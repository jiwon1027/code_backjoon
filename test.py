import sys

input = sys.stdin.readline

n,m,k = list(map(int,input().split()))
money = list(map(int,input().split()))

parent = [i for i in range(n+1)]

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a,b):
    a = find(a)
    b = find(b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

for _ in range(m):
    a,b = list(map(int,input().split()))
    union(a,b)
res = 0
friend = set()
data = dict()

for i in range(1,n+1):
    idx = find(i)
    if idx not in friend:
        data[idx] = money[i-1]
        friend.add(i)
    else:
        data[idx] = min(data[idx],money[i-1])

#print(friend)
#print(data)
res = sum(data.values())

if k < res:
    print('Oh no')
else:
    print(res)
