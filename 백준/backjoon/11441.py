import sys
input = sys.stdin.readline

n = int(input())
temp = list(map(int,input().split()))
data = [temp[0]]

for num in temp[1:]:
    data.append(data[-1]+num)
print(data)

m = int(input())
for _ in range(m):
    i,j = list(map(int,input().split()))

    if i == 1:
        print(data[j-1])
    else:
        print(data[j-1]-data[i-2])
