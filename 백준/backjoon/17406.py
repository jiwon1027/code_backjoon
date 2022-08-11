from itertools import permutations
from collections import deque
import copy


def check_min_value(arr):
    temp = []
    for i in arr:
        temp.append(sum(i))
    return min(temp)


def rotate(x, y, length):
    queue = deque()

    for i in range(y, y + length):
        queue.append(temp_data[x][i])

    for i in range(x + 1, x + length):
        queue.append(temp_data[i][y + length - 1])

    for i in range(y + length - 2, y - 1, -1):
        queue.append(temp_data[x + length - 1][i])

    for i in range(x + length - 2, x, -1):
        queue.append(temp_data[i][y])

    queue.rotate(1)

    for i in range(y, y + length):
        temp_data[x][i] = queue.popleft()

    for i in range(x + 1, x + length):
        temp_data[i][y + length - 1] = queue.popleft()

    for i in range(y + length - 2, y - 1, -1):
        temp_data[x + length - 1][i] = queue.popleft()

    for i in range(x + length - 2, x, -1):
        temp_data[i][y] = queue.popleft()


n, m, k = list(map(int, input().split()))
data = [list(map(int, input().split())) for _ in range(n)]

per = []
for _ in range(k):
    per.append(list(map(int, input().split())))
per = permutations(per)
for i in per:
    print(i)
res = 9876543210

for p in per:
    temp_data = copy.deepcopy(data)
    for rotation in p:
        r, c, s = rotation
        x = r - s - 1
        y = c - s - 1
        length = (s * 2) + 1
        while True:
            if length <= 0:
                break
            rotate(x, y, length)
            x += 1
            y += 1
            length -= 2
    res = min(check_min_value(temp_data), res)
print(res)






