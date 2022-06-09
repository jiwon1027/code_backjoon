import sys
sys.setrecursionlimit(10**6)

f = open("dict_simplified.txt", 'r')
lines = f.readlines()

word = []
explan = []

#단어, 설명 나누기
for line in lines:
    x, y = line.split('\t')
    word.append(x)
    explan.append(y)

graph = [[] for _ in range(len(word)+1)]
visited = [0] * (len(word)+1)
edge_cnt = 0
print(len(word),len(explan))
#그래프 만들기
for i in range(len(word)):
    std = word[i]
    for j in range(len(explan)):
        if std in explan[j]:
            graph[i].append(j)
            graph[j].append(i)
            edge_cnt += 1
print('Answer1 : ',len(word),edge_cnt)
max_degree = 0
idx = 0
for i, row in enumerate(graph[1:]):
    if max_degree < len(row):
        max_degree = len(row)
        idx = i
print('Answer2 : ',word[idx], max_degree)




def dfs(v,temp_edge_cnt):
    global res

    visited[v] = 1
    for i in graph[v]:
        if not visited[i]:
            dfs(i,temp_edge_cnt+1)
    return temp_edge_cnt

while True:
    if 0 in visited[1:]:
        temp_edge_cnt = 0
        edge_cnt = dfs(visited[1:].index(0)+1,temp_edge_cnt)
    else:
        print(edge_cnt)
        break




f.close()