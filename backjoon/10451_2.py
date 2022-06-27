def find(target):
    if parent[target] != target:
        parent[target] = find(parent[target])
    return parent[target]

def union(a, b):
    global ans
    a = find(a)
    b = find(b)
    if a < b:
        parent[b] = a
    elif a > b:
        parent[a] = b


for _ in range(int(input())):
    n = int(input())
    data = list(map(int,input().split()))
    parent = list(range(n+1))
    res = []

    for i in range(n):
        union(i+1,data[i])

    for i in range(n+1):
        res.append(find(i))
    print(len(list(set(res[1:]))))