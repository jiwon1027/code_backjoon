n, m, b = list(map(int, input().split()))

ground = [list(map(int, input().split())) for _ in range(n)]

from math import inf
res = inf
height = 0
start = min(map(min,ground))
end =  max(map(max,ground))

for h in range(start, end + 1):
    max_value = 0
    min_value = 0
    for i in range(n):
        for j in range(m):
            if ground[i][j] > h:
                max_value += (ground[i][j] - h)
            else:
                min_value += (h - ground[i][j])
    bag = max_value + b

    if bag < min_value:
        continue

    time = 2 * max_value + min_value

    if time <= res:
        res = time
        height = h
print(res, height)