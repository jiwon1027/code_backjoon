def distance(x,y,x1,y1):
    return abs(x-x1) + abs(y-y1)

def func():
    global charge_store,T,res
    for i in range(31):
        for j in range(31):
            if len(board[i][j]) > 1:
                flag = False
                for char in board[i][j]:
                    if not check[ord(char) - 65]:
                        flag = True
                    dist[ord(char) - 65] = min(dist[ord(char) - 65],
                                               distance(i, j, data[ord(char) - 65][0], data[ord(char) - 65][1]))
                    check[ord(char) - 65] = 1
                if flag:
                    charge_store += 1

            if charge_store > 2:
                print('#'+str(T)+' '+str(-1))
                return

for T in range(int(input())):
    N = int(input())
    board = [['.'] * 31 for _ in range(31)]
    check = [0] * N #충전 가능한지 확인 하는 배열
    dist = [0] * N #거리 최소로 만드려고 저장하는 배열
    data = []
    charge_store = 0
    res = 0

    for house in range(N):
        x,y,d = list(map(int,input().split()))
        x += 15 #index 맞쳐주기 왼쪽 맨아래가 -15 -15
        y += 15
        dist[house] = d
        data.append([x,y,d])
        for i in range(31):
            for j in range(31):
                if distance(x,y,i,j) <= d:
                    if board[i][j] != '.':
                        board[i][j] += chr(house+65)
                    else:
                        board[i][j] = chr(house+65)
    for i in board:
        print(*i)

    func()

    if check.count(0) + charge_store > 2:
        print('#' + str(T) + ' ' + str(-1))
    elif charge_store == 0:
        print('#' + str(T) + ' ' + str(2))
    else:
        for i in range(len(check)):
            if check[i]:
                res += dist[i]
            else:
                res += 1
        print('#' + str(T) + ' ' + str(res))





