n = int(input())
arr = list(map(int, input().split(' ')))
arr.sort()

answer = 1

for i in arr:
    if i == answer:
        answer += 1

print(answer)