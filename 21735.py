n,m = map(int,input().split())

data = [0] + list(map(int,input().split()))
result = 0

#백트래킹(dfs)
def dfs(i,size,time):
    global result

    if time > m:
        return
    if time <= m:
        result = max(result,size)

    if i <= n-1:
        dfs(i+1,size + data[i+1],time+1)

    if i <= n-2:
        dfs(i+2,size//2 + data[i+2], time+1)

dfs(0,1,0)
print(result)