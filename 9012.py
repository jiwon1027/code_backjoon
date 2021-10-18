n = int(input())

for _ in range(n):
    data = input()
    cnt = 0
    for x in data:
        if x == '(':
            cnt += 1
        elif x == ')':
            cnt -= 1
        if cnt < 0:
            print('NO')
            break
    if cnt == 0:
        print('YES')
    elif cnt > 0:
        print('NO')

