n = int(input())
res = []
for _ in range(n):
    data = input()
    cnt = 0
    while True:
        if data.find('for') != -1:
            data = data.replace('for', ' ',1)
            cnt += 1
        elif data.find('while') != -1:
            data = data.replace('while', ' ',1)
            cnt += 1
        else:
            break
    res.append(cnt)
print(max(res))
