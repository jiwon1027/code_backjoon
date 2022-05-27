n,k = list(map(int,input().split()))
board = [list(input()) for _ in range(2)]
visited = [[0] * n for _ in range(2)]

from collections import deque


queue = deque()
queue.append((0,0))
time = -1
while queue:
    for _ in range(len(queue)):
        line, idx = queue.popleft()
        if idx+1 >= n or idx+k >= n:
            print(1)
            exit()

        if board[line][idx+1] == '1' and not visited[line][idx+1]:
            queue.append((line,idx+1))
            visited[line][idx+1] = 1

        if board[line][idx-1] == '1' and not visited[line][idx-1] and idx-1 > time+1:
            queue.append((line,idx-1))
            visited[line][idx-1] = 1

        if board[(line+1)%2][idx+k] == '1' and not visited[0][idx+k]:
            queue.append(((line+1)%2, idx+k))
            visited[(line+1)%2][idx+k] = 1
    time += 1
print(0)


