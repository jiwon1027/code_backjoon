import sys
input = sys.stdin.readline

n,m = list(map(int,input().split()))
data = dict()
for _ in range(n):
    temp = input().strip()
    if len(temp) >= m:
        if data.get(temp):
            data[temp] += 1
        else:
            data[temp] = 1
res = sorted(data.items(),key=lambda x:(-x[1],-len(x[0]),x[0]))
for word,i in res:
    print(word)
