import heapq

n = int(input())
heap = []
cnt = 0

for _ in range(n):
    for data in list(map(int,input().split())):
        if len(heap) < n:
            heapq.heappush(heap,data)
        else:
            if heap[0] < data:
                heapq.heappop(heap)
                heapq.heappush(heap,data)
print(heap[0])
