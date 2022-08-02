import sys
input = sys.stdin.readline
n = int(input())
data = list(map(int,input().split()))
m = int(input())

end = max(data)
start = 0

while start <= end:
    mid = (start + end) // 2
    res = 0
    for i in data:
        if i > mid:
            res += mid
        else:
            res += i
    if res <= m:
        start = mid + 1
    else:
        end = mid - 1
print(end)
