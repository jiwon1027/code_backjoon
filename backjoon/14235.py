n = int(input())

import heapq
res = []

for _ in range(n):
    temp = list(map(int,input().split()))

    if temp[0] == 0:
        if len(res) > 0:
            print(-heapq.heappop(res))
        else:
            print(-1)
    else:
        if len(temp) > 0:
            for i in temp[1:]:
                heapq.heappush(res, -i)



