def multi(mat1, mat2):
    ans = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                ans[i][j] += mat1[i][k] * mat2[k][j]
            ans[i][j] %= 1000
    return ans

def divide(m,board):
    if m == 1:
        return board
    elif m == 2:
        return multi(board,board)
    else:
        temp = divide(m//2,board)

        if m%2:
            return multi(multi(temp,temp),board)
        else:
            return multi(temp,temp)


n,m = list(map(int,input().split()))
data = [list(map(int,input().split())) for _ in range(n)]

res = divide(m,data)

for row in res:
    for v in row:
        print(v%1000, end=' ')
    print()