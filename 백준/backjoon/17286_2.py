import heapq
import sys
import math

input = sys.stdin.readline
INF = int(1e9) # inf = float('int')


person = [list(map(int,input().split())) for _ in range(4)]

node, line = 4, 5
start = 0

graph = [[] for i in range(node)]
distance = [INF] * (node)

def cal(a,b):
    return int(math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2))

for i in range(node+1):
    for j in range(i+1,node):
        graph[i].append((j,cal(person[i],person[j])))

def dijkstra(start):
    q = []
    heapq.heappush(q,(0,start))
    distance[start] = 0
    while q:
        dist,now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))

dijkstra(start)

print(distance[-1])

