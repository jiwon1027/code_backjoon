n,m = list(map(int,input().split()))
board = []

for _ in range(n):
    board.append(list(input()))

board += zip(*board)

ans = ['UP','DOWN','LEFT','RIGHT']
res = 0

for i in board:
    i = ''.join(i)
    if '#.#' in i:
        print(ans[res])
    if '##' in i:
        res += 1