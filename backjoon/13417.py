from collections import deque

t = int(input())
for _ in range(t):
    n = int(input())
    card = input().split()
    queue = deque(card)

    res = deque()

    temp = queue.popleft()
    res.append(temp)
    while queue:
        temp = queue.popleft()
        if temp > res[0]:
            res.append(temp)
        else:
            res.appendleft(temp)
    for i in res:
        print(i,end='')
    print()