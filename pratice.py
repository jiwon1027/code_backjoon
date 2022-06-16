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

graph = [[] for _ in range(len(word))]
visited = [0] * len(word)
edge_cnt = 0

#그래프 만들기
for i in range(len(word)):
    std = word[i]
    for j in range(len(explan)):
        if std in explan[j]:
            graph[i].append(j)
            edge_cnt += 1
print('Answer1 : ',len(word), edge_cnt//2)

# 차수 max값 찾기
max_degree = 0
idx = 0
for i, row in enumerate(graph):
    if max_degree < len(row):
        max_degree = len(row)
        idx = i
print('Answer2 : ',word[idx], max_degree)

# connected componet는 dfs로 탐색하여 max()로 필터링
temp_conn_cnt = 0
conn_cnt = 0
def conn_dfs(v):
    global temp_conn_cnt

    visited[v] = 1
    for i in graph[v]:
        if not visited[i]:
            temp_conn_cnt += 1
            conn_dfs(i)
    return temp_conn_cnt

while True:
    if 0 in visited[1:]:
        conn_cnt = max(conn_cnt,conn_dfs(visited[1:].index(0)+1))
    else:
        print('Answer3 : ',conn_cnt)
        break

# k의 길이만큼 탐색
std_word, k = input('Answer4 : ').split()
visited = [0] * len(word)

temp_res = set()

def dfs(v,depth):
    if depth == int(k):
        return

    visited[v] = 1

    for i in graph[v]:
        if not visited[i]:
            temp_res.add(i)
            dfs(i,depth+1)
dfs(word.index(std_word),0)

print(std_word)
for i in temp_res:
    print(word[i])


f.close()