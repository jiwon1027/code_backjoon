n = int(input())
data = sorted(list(map(int, input().split())))
q, r = divmod(n, 2)
print(data[q+r-1])

n = int(input())
data = sorted(list(map(int, input().split())))
if n % 2:
    print(data[n//2])
else:
    print(data[n//2 -1])