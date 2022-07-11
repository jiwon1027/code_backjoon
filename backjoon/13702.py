import sys
input = sys.stdin.readline

n,k = list(map(int,input().split()))
data = []
for _ in range(n):
    data.append(int(input()))
start = 1
end = max(data)
res = 0

while start <= end:
    mid = (start+end) // 2
    cnt = 0
    temp = sum(i // mid for i in data)

    if temp < k:
        end = mid - 1
    else:
        res = mid
        start = mid + 1
print(res)