#우측 하단만 이동 가능
'''


costs = [[1,2,3],[4,5,6],[7,8,9]]
xcost = 1
ycost = 1
result = 25
costs = [[1,2,3],[4,5,6],[7,8,9]]
xcost = 100
ycost = 0
result = 12

'''

costs = [[0,0,0],[0,0,0],[0,0,1]]
xcost = 0
ycost = 0
result = 1

def solution(costs, xcost, ycost):
    n = len(costs)
    dp = [[0] * n for _ in range(n)]

    for x in range(n):
        for y in range(n):
            if x == n - 1:

                if 0 <= y + 1 < n:
                    if costs[x][y] >= xcost:
                        dp[x][y + 1] = dp[x][y] + costs[x][y] - xcost
                    else:
                        return dp[x][y] + costs[x][y]
                else:
                    return dp[x][y] + costs[x][y]

            if 0 <= x + 1 < n:
                if costs[x][y] > ycost:
                    dp[x + 1][y] = dp[x][y] + costs[x][y] - ycost
            if 0 <= y + 1 < n:
                if costs[x][y] > xcost:
                    dp[x][y + 1] = dp[x][y] + costs[x][y] - xcost

print(solution(costs,xcost,ycost))


