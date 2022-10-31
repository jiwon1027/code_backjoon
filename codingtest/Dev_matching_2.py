## 영토 가중치 똑같으면 알파벳 순서가 느리면 승리
## 자신보다 영토가 작은 나라 점령



def solution(maps):

    def bfs(res,N,M,i,j,visited):
        from collections import deque
        from collections import Counter

        dx = [1,-1,0,0]
        dy = [0,0,1,-1]
        temp = []

        queue = deque()
        visited[i][j] = True
        queue.append((i,j))
        temp.append(maps[i][j])

        while queue:
            x,y = queue.popleft()

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0<=nx<N and 0<=ny<M and not visited[nx][ny]:
                    if not maps[nx][ny] == '.':
                        visited[nx][ny] = True
                        queue.append((nx,ny))
                        temp.append(maps[nx][ny])

        check_temp = Counter(temp)
        check = list(check_temp.items())
        check.sort(key=lambda x: (x[1],x[0]))
       # print(check)
        std_country = check[-1][0]
        std_value = check[-1][1]

        sum = std_value
        for country, value in check:
            if value < std_value and std_country != country:
                sum += value
            elif value >= std_value and std_country != country:
                res.append((country, value))

        res.append((std_country,sum))


    res = []
    N = len(maps)
    M = len(maps[0])

    visited = [[False] * M for _ in range(N)]
    for i in range(N):
        for j in range(M):
             if not maps[i][j] == '.' and not visited[i][j]:
                 bfs(res,N,M,i,j,visited)
    res.sort(key=lambda x: (x[1],x[0]))
    dic = dict()

    for country, value in res:
        if dic.get(country):
            dic[country] += value
        else:
            dic[country] = value
    #print(dic)
    return dic[max(dic, key=dic.get)]


maps = ["AABCA.QA", "AABC..QX", "BBBC.Y..", ".A...T.A", "....EE..", ".M.XXEXQ", "KL.TBBBQ"]
#maps = ["XY..", "YX..", "..YX", ".AXY"]
print(solution(maps))