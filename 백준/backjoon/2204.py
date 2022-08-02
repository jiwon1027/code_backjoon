while True:
    data = []
    n = int(input())
    if n == 0:
        exit()
    for _ in range(n):
        data.append(input())
    data.sort(key=str.lower)
    print(data[0])