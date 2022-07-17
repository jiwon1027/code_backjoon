'''
문자열로 보고 1 1 1을 찾으려고 했지만 1 1 1 1 같은 상황에서 예외처리를 하기 힘들어서
그냥 1을 counting 하기로함
'''
def count_board(board):
    res = 0

    for row in board:
        cnt = 0
        for idx,tmp in enumerate(row):
            if tmp:
                cnt += 1
            if not tmp or idx == n-1:
                if cnt == k:
                    res += 1
                cnt = 0
    return res

for z in range(int(input())):
    n,k = list(map(int,input().split()))
    board = [list(map(int,input().split())) for _ in range(n)]

    res = count_board(board) + count_board(list(map(list,zip(*board))))

    ans = f'#{z+1} {res}'
    print(ans)