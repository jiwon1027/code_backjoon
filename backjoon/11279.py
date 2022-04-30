import sys
import heapq

input = sys.stdin.readline

n = int(input())
heap = []
for _ in range(n):
    temp = int(input())
    if temp != 0:
        heapq.heappush(heap, -temp)
    else:
        try:
            print(-heapq.heappop(heap))
        except:
            print(0)