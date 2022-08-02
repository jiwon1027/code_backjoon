
a,b,c = list(map(int,input().split()))
time = [0] * 101
for _ in range(3):
    start, end = list(map(int,input().split()))
    for i in range(start,end):
        time[i] += 1
#print(time)
res = 0
for i in time:
    if i == 1:
        res += i * a
    elif i == 2:
        res += i * b
    elif i == 3:
        res += i * c
print(res)