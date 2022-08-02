import sys
input = sys.stdin.readline

n,m,s = list(map(int,input().split()))

time = [(0,0)]
for _ in range(n):
    x,y = list(map(int,input().split()))
    time.append((x,x+y))
time.append((s,s))
time.sort()
#print(time)

for i in range(len(time)-1):
    #print(time[i+1][0] - time[i][1])
    if (time[i+1][0] - time[i][1]) >= m:
        print(time[i][1])
        break
else:
    print(-1)