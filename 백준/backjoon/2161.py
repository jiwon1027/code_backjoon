n = int(input())

from collections import deque

queue = deque(range(1,n+1))

while len(queue) > 1:
    print(queue.popleft(), end=' ')
    queue.append(queue.popleft())
print(queue[0])
