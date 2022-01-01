def check(arr):
    n = len(arr)
    answer = 1
    # 열 검사
    for i in range(n):
        result = 1
        for j in range(1, n):
            if arr[i][j] == arr[i][j - 1]:
                result += 1
            else:
                result = 1

            if result > answer:
                answer = result
            # 행 검사
        result = 1
        for j in range(1, n):
            if arr[j][i] == arr[j - 1][i]:
                result += 1
            else:
                result = 1

            if result > answer:
                answer = result
    return answer


n = int(input())
answer = 0
board = [list(input()) for _ in range(n)]

# 입력받은 보드에서 인접한거 하나씩 바꿔가면서 check() 수행
# 열 바꿔보기
for i in range(n):
    for j in range(n):
        if j + 1 < n:
            board[i][j], board[i][j + 1] = board[i][j + 1], board[i][j]
            result = check(board)
            if result > answer:
                answer = result
            board[i][j], board[i][j + 1] = board[i][j + 1], board[i][j]
        # 행 바꿔보기
        if i + 1 < n:
            board[i][j], board[i + 1][j] = board[i + 1][j], board[i][j]
            result = check(board)
            if result > answer:
                answer = result
            board[i][j], board[i + 1][j] = board[i + 1][j], board[i][j]
print(answer)






