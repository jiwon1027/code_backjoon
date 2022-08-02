A, B = list(map(int,input().split()))
m = int(input())
data = list(map(int,input().split()))[::-1]

res = 0
for i in range(m):
    res += data[i] * (A**i)

temp = []
while res != 0:
    temp.append(res % B)
    res //= B

print(*temp[::-1])
