n = int(input())
'''
#이런식으로 푸는거 아닌듯?
data = [0] * 100001
for _ in range(n):
    x,y = list(map(int,input().split()))
    for i in range(x,y+1):
        data[i] += 1
'''
start,end = 0, 100000
for _ in range(n):
    x,y = list(map(int,input().split()))
    start = max(start, x)
    end = min(end, y)
if start-end < 0:
    print(0)
else:
    print(start-end)

