t = int(input())
for _ in range(t):
    start_x, start_y, end_x, end_y = list(map(int,input().split()))
    n = int(input())
    res = 0
    for _ in range(n):
        x, y, r = list(map(int,input().split()))
        d_start_to_planet = (((x-start_x) **2) + ((y - start_y) **2)) ** 0.5
        d_planet_to_end = (((x-end_x) **2) + ((y - end_y) **2)) ** 0.5
        if (d_planet_to_end > r and d_start_to_planet < r) or (d_planet_to_end < r and d_start_to_planet > r):
            res += 1
    print(res)
