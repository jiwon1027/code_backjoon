n = int(input())
ticket = list(map(int,input().split()))
ticket.sort()

res = 0

# 우선순위 큐
for i in range(n):
    if ticket[i] != i+1:
        print(i+1)
        res += 1
        break
else:
    print(n+1)