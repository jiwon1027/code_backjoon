def end_check():
    for i in range(12):
        if alphbet[i] == -1:
            return False
    return True

def line_sum_check():
    for i in range(6):
        sum = 0
        for j in range(4):
            sum += alphbet[line_idx_list[i][j]-1]
        if not sum == 22: ## 26-4
            return False
    return True

def print_answer():
    idx = 0
    for i in range(5):
        if (i == 0 or i == 4):
            for j in range(9):
                if j ==4:
                    print(chr(alphbet[idx]+65),end='')
                    idx += 1

                else:
                    print('.',end='')
        elif i == 1 or i==3:
            for j in range(9):
                if j%2==1:
                    print(chr(alphbet[idx]+65),end='')
                    idx += 1

                else:
                    print('.',end='')
        elif i==2:
            for j in range(9):
                if j==2 or j==6:
                    print(chr(alphbet[idx]+65),end='')
                    idx += 1

                else:
                    print('.',end='')
        print()
def dfs():
    if (end_check() and line_sum_check()):
        print_answer()
        exit()
        return

    for temp_data in range(12): # A~L까지 사전순으로 하나씩 넣어보겠다
        if visited[temp_data]:
            continue
        for j in range(12): # 첫번째칸부터 하나씩 순차적으로 넣어보겠다
            if alphbet[j] == -1:
                alphbet[j] = temp_data
                visited[temp_data] = True
                dfs()
                alphbet[j] = -1
                visited[temp_data] = False
                break


board = []
for _ in range(5):
    board.append(input())
line_idx_list = [[2,3,4,5], [5,7,10,12],[2,6,9,12],[8,9,10,11],[1,3,6,8],[1,4,7,11]]

alphbet = [0] * 12
visited = [False] * 12
idx = 0

for row in board:
    for col in row:
        if not col == '.':
            if col == 'x':
                alphbet[idx] = -1
            else:
                alphbet[idx] = ord(col)-65
                visited[ord(col)-65] = True
            idx+=1

dfs()

