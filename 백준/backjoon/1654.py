k, n = list(map(int,input().split()))

data = [int(input()) for _ in range(k)]
start, end = 1, max(data)

while start <= end:
    mid = (start + end) // 2
    lines = 0

    for i in data:
        lines += i // mid
    if lines < n:
        end = mid - 1
    else:
        start = mid + 1
print(end)