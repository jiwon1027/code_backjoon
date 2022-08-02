from bisect import bisect_left

n = int(input())
ticket = list(map(int,input().split()))
ticket.sort()

# 이진탐색
max_value = ticket[-1]

for i in range(1, max_value+1):
    index = bisect_left(ticket,i)

    if index < n and ticket[index] != i:
        print(i)
        break
    if index == n-1:
        print(max_value + 1)

