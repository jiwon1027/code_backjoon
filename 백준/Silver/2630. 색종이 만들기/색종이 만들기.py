n = int(input())
board = []
for _ in range(n):
    board.append(list(map(int,input().split())))

color_temp = 0
white_color = 0
blue_color = 0

def divide_conquer(x,y,n):
    global white_color
    global blue_color
    color_temp = board[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if color_temp != board[i][j]:
                divide_conquer(x,y,n//2)
                divide_conquer(x,y+n//2,n//2)
                divide_conquer(x+n//2,y,n//2)
                divide_conquer(x+n//2,y+n//2,n//2)
                return
    if color_temp == 1:
        white_color += 1
    else:
        blue_color += 1
divide_conquer(0,0,n)
print(blue_color)
print(white_color)
