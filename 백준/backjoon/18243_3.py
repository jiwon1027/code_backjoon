import sys

n, k = list(map(int,input().split()))

edges = [list(map(int,input().split())) for _ in range(k)]
INF = sys.maxsize

def make_graph():
    graph = [[INF] * n for _ in range(n)]

    for frm, to in edges:
        graph[frm-1][to-1] = 1
        graph[to-1][frm-1] = 1

    return graph

def floyd(graph):
    for v in range(n):
        graph[v][v] = 0

    for k in range(n):
        for u in range(n):
            for v in range(n):
                graph[u][v] = min(graph[u][v], graph[u][k] + graph[k][v])

def solution():
    graph = make_graph()
    floyd(graph)

    for frm in range(n):
        for to in range(n):
            if graph[frm][to] > 6:
                return 'Big World!'
    return 'Small World!'

print(solution())


