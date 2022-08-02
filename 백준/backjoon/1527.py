from collections import deque
a,b = list(map(int,input().split()))

queue = deque([4,7])
res = 0

while queue:
    v = queue.popleft()
    if v <= b:
        if a <= v:
            res += 1
        queue.append(v*10 + 4)
        queue.append(v*10 + 7)
print(res)


