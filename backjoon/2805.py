import sys
input = sys.stdin.readline

n,m = list(map(int,input().split()))
tree = list(map(int,input().split()))
start, end = 1, max(tree)

while start <= end:
    mid = (start + end) // 2

    res = 0

    for i in tree:
        if i >= mid:
            res += i - mid

    if res >= m:
        start = mid + 1
    else:
        end = mid - 1
print(end)