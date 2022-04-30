#단순 분할정복 (시간초과)
#모든 칸을 방문하기 때문에 불필요한 연산이 지속됨
def divide(x, y, size):
    global cnt
    if size == 2:
        if x == r and y == c: # 2사분면
            print(cnt)
            return
        cnt += 1
        if x == r and y + 1 == c: # 1사분면
            print(cnt)
            return
        cnt += 1
        if x + 1 == r and y == c: # 3사분면
            print(cnt)
            return
        cnt += 1
        if x + 1 == r and y + 1 == c: # 4사분면
            print(cnt)
            return
        cnt += 1
    else:
        divide(x, y, size//2) # 2사분면
        divide(x, y + size//2, size//2) # 1사분면
        divide(x + size//2, y, size//2) # 3사분면
        divide(x + size//2, y + size//2, size//2) # 4사분면



n, r, c = list(map(int,input().split()))
cnt = 0
divide(0,0,2**n)

