def check(paper):
    N = len(paper)
    if N == 1:
        return True
    mid = N//2
    for i in range(mid):
        if paper[i] == paper[-i - 1]:
            return False
    return check(paper[:mid])


n = int(input())
for _ in range(n):
    temp = input()
    if check(temp):
        print('YES')
    else:
        print('NO')