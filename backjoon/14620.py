n = int(input())
cost = []
for _ in range(n):
    cost.append(list(map(int,input().split())))

#dx, dy를 현재 위치인 0,0까지 포함해서 두고
#백트래킹 돌려보자

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
def fun(x,y,visited):
    cost_value = 0
    cnt = 0
    for i in range(x,n-1):
        for j in range(y,n-1):
            if cnt == 3:
                return cost_value

            flag = 1
            for k in range(4):
                nx = i + dx[k]
                ny = j + dy[k]
                if not ((0 <= nx < n and 0 <= ny < n) and not visited[nx][ny] and not visited[i][j]):
                    flag = 0
                    break
            if flag == 1:
                print(i, j)
                visited[i][j] = 1
                cost_value += cost[i][j]
                for k in range(4):
                    nx = i + dx[k]
                    ny = j + dy[k]
                    visited[nx][ny] = 1
                    cost_value += cost[nx][ny]
                cnt += 1

    return cost_value

data = []
for i in range(1, n-1): #n-1 x n-1 사이에서 브루트포스 해야됨
    for j in range(1, n-1):
        visited = [[0] * n for _ in range(n)]
        data.append(fun(i,j,visited))
        print()
print(data)
print(min(data))


