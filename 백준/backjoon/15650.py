def DFS(j):
    if len(s) == M:
        print(*s)
        return

    for i in range(j, N + 1):
        if i in s: #가지치기
            continue

        s.append(i)
        DFS(i+1)  # 함수 다시 호출
        s.pop()  # 원상복귀

N, M = map(int, input().split())
s = []  # 출력 수열 넣을 stack
DFS(1)