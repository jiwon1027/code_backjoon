from collections import deque

a,b = list(map(int,input().split()))

queue = deque()
queue.append((a,1))

while queue:
    v,r = queue.popleft()

    if v > b:
        continue
    if v == b:
        print(r)
        break

    queue.append((2*v,r+1))
    queue.append((int((str(v)+'1')),r+1))
else:
    print(-1)