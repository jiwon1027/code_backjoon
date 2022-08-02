t = int(input())
def recursive(num):
    global cnt
    if num < 10:
        if num == 0:
            cnt += 1
    else:
        recursive(num // 10)
        recursive(num % 10)


for _ in range(t):
    n , m = map(int, input().split())
    cnt = 0
    for i in range(n,m+1):
        recursive(i)

    print(cnt)