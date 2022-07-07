n = int(input())
data = sorted(list(map(int, input().split())))
if n % 2:
    print(data[n//2])
else:
    print(data[n//2 -1])