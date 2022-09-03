def bfs(temp_list):
    queue = deque([temp_list[0]])
    visited = [0] * (n+1)
    visited[temp_list[0]] = 1

    while queue:
        v = queue.popleft()

        for i in graph[v]:
            if not visited[i] and i in temp_list:
                queue.append(i)
                visited[i] = 1

    for i in temp_list:
        if visited[i] == 1:
            continue
        else:
            return False
    else:
        return True

n = int(input())
cost = list(map(int,input().split()))

graph = [[] for _ in range(n+1)]
city = [i for i in range(1,n+1)]

for i in range(1,n+1):
    temp = list(map(int,input().split()))
    for num in temp[1:]:
        graph[i].append(num)
        graph[num].append(i)


def fun(n):
    return cost[n-1]

from itertools import combinations
from collections import deque

res = 10000
for i in range(1, n//2+1):
    for combi in list(combinations(city,i)):
        A = []
        B = [i for i in range(1, n + 1)]
        for j in combi:
            A.append(j)
            B.remove(j)
        if bfs(A) and bfs(B):
            res = min(res, abs(sum(list(map(fun,A))) - sum(list(map(fun,B)))))
if res == 10000:
    print(-1)
else:
    print(res)

'''   
#유니온 파인드 써서 필터링 하고 모든 경우데 대해 고려한 풀이였는데 잘못된 접근
#유니온 파인드

parent = [i for i in range(n+1)]

def find(target):
    if parent[target] != target:
        parent[target] = find(parent[target])
    return parent[target]


def union(a, b):
    a = find(a)
    b = find(b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

for i in range(1,n+1):
    temp = list(map(int,input().split()))
    for num in temp[1:]:
        graph[i].append(num)
        union(i,num)
# 루트 노드 찾기
for i in range(1,n+1):
    find(i)

#유니온-파인드로 필터링
if len(set(parent[1:])) == 2:
    idx_1 = list(set(parent[1:]))[0]
    idx_2 = list(set(parent[1:]))[1]
    sum = 0
    for idx, value in enumerate(parent[1:]):
        if value == idx_1:
            sum += cost[idx]
        if value == idx_2:
            sum -= cost[idx]
    print(abs(sum))
    exit()
elif len(set(parent[1:])) > 1 or len(set(parent[1:])) == 0:
    print(-1)
    exit()
else: #모든 노드가 이어져 있을 때
    temp_case = set()
    res = 0
    for i in range(1,n+1):
        if len(graph[i]) == 1:
            res = min(res, sum(cost) - cost[i-1])
            res = min(res, sum(cost) - cost[graph[i][0] - 1] - cost[i - 1])

            temp_case.add((graph[i][0],i))
            temp_case.add((i,graph[i][0]))
        else:
            print('아 이거 아닌거같아. 뭔가 이런 브루트포스적인 문제는 아닌거같음')
'''


