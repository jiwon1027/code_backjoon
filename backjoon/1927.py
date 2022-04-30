import heapq
import sys

input = sys.stdin.readline
heap = []

n = int(input())
for _ in range(n):
    temp = int(input())
    if temp != 0:
        heapq.heappush(heap,temp)
    else:
        try:
            print(heapq.heappop(heap))
        except:
            print(0)
