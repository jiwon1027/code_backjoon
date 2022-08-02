n,k = map(int,input().split())
data = []
for i in range(1,n+1):
    if n % i == 0:
        data.append(i)
try:
    print(data[k-1])
except:
    print(0)
