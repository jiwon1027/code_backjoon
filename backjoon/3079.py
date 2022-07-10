import sys
input = sys.stdin.readline

N, M = map(int, input().split())
time = sorted(list(int(input()) for _ in range(N)))

start = 0
end = min(time) * M
result = 0

while start <= end :
    mid = (start + end) // 2
    temp = 0
    for t in time:
        temp += mid // t

    if temp >= M:
        end = mid - 1
        result = mid #sorted했기 때문에 min()해줄 필요 x
    else:
        start = mid + 1
    #print(start,end)
print(result)