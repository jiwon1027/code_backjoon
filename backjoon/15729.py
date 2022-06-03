n = int(input())

data = list(map(int,input().split()))

temp = [0] * n

res = 0
for i in range(n):
    if data[i] != temp[i]:
        res += 1
        temp[i] = not temp[i]

        if i+1 < n:
            temp[i+1] = not temp[i+1]
        if i+2 < n:
            temp[i+2] = not temp[i+2]
print(res)




