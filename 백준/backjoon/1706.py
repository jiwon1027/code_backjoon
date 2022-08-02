r,c = list(map(int,input().split()))

board = [list(map(str,input())) for _ in range(r)]
res = []
for i in range(r):
    if '#' not in board[i]:
        res.append(''.join(board[i]))
    else:
        temp = ''
        for j in board[i]:
            if j != '#':
                temp += j
            else:
                if len(temp) > 1:
                    res.append(temp)
                temp = ''
        if len(temp) > 1:
            res.append(temp)

change_data = list(map(list, zip(*board)))
for i in range(c):
    if '#' not in change_data[i]:
        res.append(''.join(change_data[i]))
    else:
        temp = ''
        for j in change_data[i]:
            if j != '#':
                temp += j
            else:
                if len(temp) > 1:
                    res.append(temp)
                temp = ''
        if len(temp) > 1:
            res.append(temp)


print(sorted(res)[0])




