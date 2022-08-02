def dfs():
    if len(stack) == m:
        print(*stack)
        return


    for i in range(1,n+1):
        stack.append(i)
        dfs()
        stack.pop()


n,m = map(int,input().split())
stack = []
dfs()