n,m = list(map(int,input().split()))
j = int(input())

left = 1
right = m
res = 0

for _ in range(j):
    location = int(input())

    if left <= location <= right:
        continue
    if left > location:
        res += (left - location)
        right -= (left - location)
        left = location
    else:
        res += (location - right)
        left += (location - right)
        right = location
print(res)




