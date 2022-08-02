def fun(board,n):
    if n == 1:
        return board[0][0]

    new_data = [[] for _ in range(n//2)]
    for i in range(0,n,2):
        for j in range(0,n,2):
            new_data[i//2].append(sorted([board[i][j],board[i+1][j],board[i][j+1],board[i+1][j+1]])[2])

    return fun(new_data,n//2)

n = int(input())
board = []
for _ in range(n):
    board.append(list(map(int,input().split())))
print(fun(board,n))


'''
print(board[0][0:2])
print(board[1][0:2])

print(board[0][2:4])
print(board[1][2:4])

print(board[2][0:2])
print(board[3][0:2])

print(board[2][2:4])
print(board[3][2:4])
'''
