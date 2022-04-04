n = int(input())

data = list(map(int,input().split()))
data = set(data)
data = list(data)

data.sort()
print(*data)