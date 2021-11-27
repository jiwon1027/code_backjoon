def DFS(data,j):
    if len(s) == M:
        print(*s)
        return

    for i in range(j,len(data)):
        if i in s: #가지치기
            continue

        s.append(data[i])
        DFS(data,i+1)  # 함수 다시 호출
        s.pop()  # 원상복귀

N, M = map(int, input().split())
data = list(map(int,input().split()))
data.sort()
s = []  # 출력 수열 넣을 stack
DFS(data,0)