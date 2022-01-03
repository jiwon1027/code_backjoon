n, m = map(int, input().split())
limit_stu = [0] + list(map(int,input().split()))
sugang = [[] for _ in range(m + 1)]
result = [[] for _ in range(n + 1)]

for _ in range(2):
    import copy
    temp = copy.deepcopy(sugang)

    for i in range(n):
        data = list(map(int,input().split()))
        for j in range(len(data) - 1):
            temp[data[j]].append(i + 1)

    for i in range(1, m + 1):
        if len(temp[i]) <= limit_stu[i]:
            sugang[i] = temp[i]
        else:
            limit_stu[i] = 0



for i in range(m + 1):
    for x in sugang[i]:
        result[x].append(i)
for i in range(1, n + 1):
    if len(result[i]):
        print(*result[i])
    else:
        print('망했어요')