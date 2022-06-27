def check(k):
    temp = ''
    for x in range(5):
        for y in range(3):
            temp += str(board[x][k+y])
    #print('k',k)
    if k == width-1:
        return 1

    if temp in array:
        return array.index(temp)
    else:
        return 1

array = ['111101101101111','','111001111100111','111001111001111','101101111001001','111100111001111','111100111101111','111001001001001','111101111101111','111101111001111']
n = int(input())
data = input()

width = n // 5


board = [[0] * width for _ in range(5)]

for i in range(n):
    if data[i] == '#':
        board[i//width][i%width] = 1
idx = 0
while idx < width:
    if board[0][idx] == 1:
        print(check(idx),end='')
        idx += 3
    else:
        idx += 1

        number = [data[i * (length // 5): (i + 1) * (length // 5)] for i in range((length + (length // 5) - 1) // (length // 5))]
