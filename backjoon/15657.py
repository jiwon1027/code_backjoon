n, m = map(int, input().split())
data = list(map(int, input().split()))
data.sort()
res = []

def Dfs(depth):
    if depth == m:
        print(' '.join(map(str, res)))
        return

    for i in range(n):
        if depth == 0 or res[depth - 1] <= data[i]:
            res.append(data[i])
            Dfs(depth + 1)
            res.pop()
Dfs(0)