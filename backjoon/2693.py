n = int(input())

for _ in range(n):
    data = list(map(int,input().split()))
    data.sort()
    print(data[-3])