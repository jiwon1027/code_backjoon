n,m = list(map(int,input().split()))
board = [[i+10*j for i in range(1,11)] for j in range(10)]
ladder = []
snake = []

for _ in range(n):
    ladder.append(list(map(int,input().split())))
for _ in range(m):
    snake.append(list(map(int,input().split())))




