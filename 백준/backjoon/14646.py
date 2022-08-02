n = int(input())
menu = list(map(int,input().split()))

check = [0] * (2 * n)
cnt = 0
result = 0

for i in menu:
    if not check[i]:
        cnt += 1
        check[i] = 1

    else:
        cnt -= 1
        check[i] = 0

    result = max(result, cnt)

print(result)