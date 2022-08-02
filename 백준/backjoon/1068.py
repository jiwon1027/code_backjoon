import sys
input = sys.stdin.readline

def dfs(num, arr):
    arr[num] = -2
    for i in range(len(arr)):
        if num == arr[i]:
            dfs(i, arr)

n = int(input())
data = list(map(int, input().split()))
k = int(input())
res = 0

dfs(k, data)
for i in range(len(data)):
    if data[i] != -2 and i not in data:
        res += 1
print(res)