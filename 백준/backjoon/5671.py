while True:
    try:
        n, m = list(map(int, input().split()))
    except:
        break
    res = 0
    for i in range(n, m + 1):
        answer = set()
        temp = str(i)

        for j in temp:
            answer.add(j)
        if len(temp) == len(answer):
            res += 1

    print(res)
