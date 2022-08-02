import sys

input = sys.stdin.readline

n = int(input())

data = []
for _ in range(n):
    a,b = list(map(int,input().split()))
    data.append([a,b])
data.sort()

'''
배정된 여러 강의실이 있으면, 
그 중 시간이 가장 많이 남는
(배정된 수업의 끝나는 시간이 가장 이른) 곳에
배정하는것이 이득인게 포인트가 될 수 있을 것
'''

import heapq
heap = []

heapq.heappush(heap,data[0][1])
for i in range(1,n):
    if heap[0] > data[i][0]:
        heapq.heappush(heap,data[i][1])
    else:
        heapq.heappop(heap)
        heapq.heappush(heap,data[i][1])
print(len(heap))