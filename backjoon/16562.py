'''
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

#parent를 루트 노드로 바꿔주려고 한번 더 find했는데 이렇게 하는게 아닌가(시간초과)
for i in range(1,n+1):
    find(i)

set_parent = list(set(parent))
#print(set_parent)

res = 0
for root in set_parent[1:]:
    cost_temp = []
    for i, value in enumerate(parent[1:]):
        if value == root:
            cost_temp.append(money[i])
    res += min(cost_temp)

# res를 다 구해서 판별하는거 보다 중간에서 값 넘어갈 때 짤라도 되겠는데?
if k < res:
    print('Oh no')
else:
    print(res)
'''


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



