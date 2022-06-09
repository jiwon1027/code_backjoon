def greedy_knapsack(temp,w):
    temp.sort(key = lambda x : -(x[0] / x[1]))
    res = 0
    weight = 0
    for x,y in temp:
        if weight + x > w:
            return res
        else:
            weight += x
            res += y


def dynamic_knampscak(temp):
    for i in range(1,N+1):
        for j in range(1,K+1):

            if temp[i-1][0] <= j:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-temp[i-1][0]] + temp[i-1][1])

            else:
                dp[i][j] = dp[i-1][j]

    return dp[N][K]

import sys

N, K = 7, 15

dp = [[0 for _ in range(K+1)] for _ in range(N+1)]

items = [[2,10],[3,5],[5,15],[7,7],[1,6],[4,18],[1,3]]



print('Greedy : ', greedy_knapsack(items,K))
print('DP : ',dynamic_knampscak(items))