n = int(input())

roads = list(map(int,input().split()))
costs = list(map(int,input().split()))

result = 0
temp = costs[0]

for i in range(n-1):
    if costs[i] < temp:
        temp = costs[i]
    result += temp * roads[i]


print(result)