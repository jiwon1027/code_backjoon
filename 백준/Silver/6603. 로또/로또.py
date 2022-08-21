while True:
    data = list(map(int, input().split()))
    if data[0] == 0:
        break
    from itertools import combinations
    for i in combinations(data[1:],6):
        print(*i)
    print()