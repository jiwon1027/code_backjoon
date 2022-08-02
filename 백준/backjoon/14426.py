import sys
input = sys.stdin.readline

n,m = list(map(int,input().split()))
data = []
for _ in range(n):
    data.append(input().strip())
res = 0
for _ in range(m):
    temp = input().strip()
    length = len(temp)
    for i in data:
        if i[:length] == temp:
            #print(temp)
            res += 1
            break
print(res)
