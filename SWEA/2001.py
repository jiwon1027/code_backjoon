'''
mxm 크기만큼 잘라서 가장 큰 부분 구하는 문제
N,M에 관계가 무작위라서 분할정복으로 말고 단순 4중 for문 으로 하는게 쉬워보인다

4중 for문으로 안할꺼면 애초에 data를 받을 때 n x n으로 받지말고
m x n*(n-m+1)처럼 가로로 받아서 하는 것도 방법(but, 위의 방법보다 공간복잡도 손해인듯)

'''
for t in range(int(input())):
    n,m = list(map(int,input().split()))
    data = [list(map(int,input().split())) for _ in range(n)]
    res = 0
    for i in range(n-m+1):
        for j in range(n-m+1):
            temp = 0
            for k in range(m):
                for l in range(m):
                    temp += data[i+k][j+l]
            res = max(res, temp)
    ans = f'#{t+1} {res}'
    print(ans)