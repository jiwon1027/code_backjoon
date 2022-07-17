#sliding window 개념이 생각나서 idx로 sliding 해봄
for k in range(int(input())):
    n,m = list(map(int,input().split()))
    if n<m:
        window = list(map(int, input().split()))
        fix_list = list(map(int, input().split()))
    else:
        fix_list = list(map(int, input().split()))
        window = list(map(int, input().split()))
        n,m = m,n

    res = 0
    for i in range(abs(n-m)+1):
        temp = 0
        for j in range(n):
            temp += window[j] * fix_list[i+j]
        res = max(res,temp)

    ans = f'#{k+1} {res}'
    print(ans)