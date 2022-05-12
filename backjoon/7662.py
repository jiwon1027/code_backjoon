import heapq
import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    k = int(input())
    max_heapq = []
    min_heapq = []
    visited = [0] * k
    for i in range(k):
        command, num = input().split()

        if command == 'I':
            heapq.heappush(min_heapq,(int(num),i))
            heapq.heappush(max_heapq,(-1 * int(num),i))
        else:
            if num == '1':
                while max_heapq:
                    if visited[max_heapq[0][1]] == 1:
                        heapq.heappop(max_heapq)
                    else:
                        break


                if max_heapq:
                    visited[max_heapq[0][1]] = 1
                    heapq.heappop(max_heapq)

            elif num == '-1':
                while min_heapq:
                    if visited[min_heapq[0][1]] == 1:
                        heapq.heappop(min_heapq)
                    else:
                        break
                if min_heapq:
                    visited[min_heapq[0][1]] = 1
                    heapq.heappop(min_heapq)

    while max_heapq:
            if visited[max_heapq[0][1]] == 1:
                heapq.heappop(max_heapq)
            else:
                break
    while min_heapq:
            if visited[min_heapq[0][1]] == 1:
                heapq.heappop(min_heapq)
            else:
                break

    if min_heapq and max_heapq:
        print(-max_heapq[0][0], min_heapq[0][0])
    else:
        print('EMPTY')






