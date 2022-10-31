from collections import deque

n = int(input())
queue = deque([i for i in range(1, n+1)])
# print(queue)
t = 1

for i in range(n-1):
    num = (t**3) % len(queue)  # 탈락자 자리 번호

    if num == 1:  # 첫번째 자리에 있는 사람이 탈락할 경우 재배치 필요X
        queue.popleft()

    else:
        queue.rotate(-(num-1))  # 큐 회전
        queue.popleft()

    t += 1

print(*queue)