'''
그림이 분할정복처럼 이뻐보이지만 그냥 단순 구현으로 푸는게 쉽다.
row, col, 3x3 하나씩 check 하기
'''
def row_check(data):
    for row in data:
        if sorted(row) != list(range(1,10)):
            return False
    return True
def rect_check(data):
    for i in [0,3,6]:
        for j in [0,3,6]:
            temp = []
            for k in range(3):
                for l in range(3):
                    temp.append(data[i+k][j+l])
            if sorted(temp) != list(range(1,10)):
                return False
    return True

for t in range(int(input())):
    board = [list(map(int,input().split())) for _ in range(9)]
    if row_check(board) and row_check(list(map(list,zip(*board)))) and rect_check(board):
        ans = f'#{t+1} 1'
    else:
        ans = f'#{t + 1} 0'

    print(ans)







