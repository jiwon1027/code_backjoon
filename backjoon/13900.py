n = int(input())

data = list(map(int,input().split()))

res = sum(data)
answer = 0
for i in data:
    res = res - i
    answer = answer + i * res
print(answer)


