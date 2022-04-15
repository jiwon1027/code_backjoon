data = [int(input()) for _ in range(10)]

res = 0
for i in data:
    res += i

    if res >= 100:
        if res - 100 > 100 - (res - i):
            res -= i
        break

print(res)