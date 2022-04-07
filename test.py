import sys

INF = sys.maxsize

def Floyd_Warshall():
    dist = [[INF] *n for i in range(n)]

    for i in range(n):
        for j in range(n):
            dist[i][j] = a[i][j]

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    return dist

n = 4
a = [[0,2,INF,4], [2,0,INF,5], [3,INF,0,INF],[INF,2,1,0]]

dist = Floyd_Warshall()

for i in range(n):
    for j in range(n):
        print(dist[i][j], end='')
    print()