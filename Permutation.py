def permu(depth):
    if depth == r:
        print(isSelected)
        return

    for i in range(n):
        if not visited[i]:
            isSelected[depth] = number[i]
            visited[i] = 1
            permu(depth+1)
            visited[i] = 0
n = 4
r = 2
number = [1,2,3,4]
visited = [0] * (n+1)
isSelected = [0] * r

permu(0)


