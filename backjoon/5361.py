n = int(input())
cost = [350.34,230.90,190.55,125.30,180.90]
for _ in range(n):
    data = list(map(int,input().split()))
    total = 0
    for i in range(5):
        total += data[i] * cost[i]
    print(f'${total:.2f}')  #f-string