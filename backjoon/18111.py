from math import inf
import sys

N, M, B = map(int, input().split())
ground = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

tall = 0
ans = inf

for i in range(257):
    max = 0
    min = 0
    for j in range(N):
        for k in range(M):
            if ground[j][k] < i:
                min += (i - ground[j][k])  # 현재 높이가 블록 높이보다 높을 때 (min 만큼 인벤토리에서 꺼내서 채워야 함)
            else:
                max += (ground[j][k] - i)  # 블록 높이가 현재 높이보다 높을 때 (max 만큼 블록이 제거 후 인벤토리에 들어감)

    inventory = max + B

    if inventory < min:
        continue

    time = 2 * max + min

    if time <= ans:
        ans = time
        tall = i

print(ans, tall)