import sys
input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))

maxdata = 0
result = 0
cnt = 0

for i in data:
    if i > maxdata:
        maxdata = i
        cnt = 0
    else:
        cnt +=1

    result=max(result,cnt)

print(result)