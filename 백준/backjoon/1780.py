def divide_paper(x,y,n):
    std = paper[x][y]

    for i in range(x,x+n):
        for j in range(y,y+n):
            if paper[i][j] != std:
                for a in range(3):
                    for b in range(3):
                        divide_paper(x+a*n//3, y+b*n//3, n//3)
                return
    if std == -1:
        data[0] += 1
    elif std == 0:
        data[1] += 1
    else:
        data[2] += 1


n = int(input())

paper = []
data = [0,0,0]
for _ in range(n):
    paper.append(list(map(int,input().split())))

divide_paper(0,0,n)
for i in data:
    print(i)