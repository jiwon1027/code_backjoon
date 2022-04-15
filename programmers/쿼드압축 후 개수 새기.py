def solution(arr):
    import sys
    sys.setrecursionlimit(10 ** 6)
    data = [0, 0]

    def divide_arr(x, y, n):
        std = arr[x][y]

        for i in range(x, x + n):
            for j in range(y, y + n):
                if std != arr[i][j]:
                    for a in range(2):
                        for b in range(2):
                            divide_arr(x + a * n // 2, y + b * n // 2, n // 2)
                    return
        data[std] += 1

    divide_arr(0, 0, len(arr))

    return data

arr = [[1,1,0,0],[1,0,0,0],[1,0,0,1],[1,1,1,1]]


#arr = [[1,1,1,1,1,1,1,1],[0,1,1,1,1,1,1,1],[0,0,0,0,1,1,1,1],[0,1,0,0,1,1,1,1],[0,0,0,0,0,0,1,1],[0,0,0,0,0,0,0,1],[0,0,0,0,1,0,0,1],[0,0,0,0,1,1,1,1]]