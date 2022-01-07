n,m = map(int,input().split())

board = [list(map(str,input().split())) for _ in range(n)]

print(board)
row = []
column = []

result = 0
for i in range(n):
    temp = 0
    for k in board[i]:
        temp += k.count('9')
    row.append(temp)

print(row)
for j in range(m):
    temp = 0
    for i in range(n):
        temp += board[i][j].count('9')
    column.append(temp)
print(column)

print(sum(row) - max(max(row), max(column)))

