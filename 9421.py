num = int(input())

prime_num = []
prime = [True] * (num+1)

def isprime(n):
    n += 1
    for i in range(2, int(n ** 0.5) + 1):
        if prime[i]:
            for j in range(2 * i, n, i):
                prime[j] = False
    for i,value in enumerate(prime):
        if value:
            prime_num.append(i)
isprime(num)

ans=[]

for i in prime_num[2:]:
    visited = dict()
    temp = str(i)
    while True:
        #각 자리수 제곱
        tmp = sum(map(lambda x: int(x) ** 2, temp))
        idx = int(temp)
        if tmp == 1:
            ans.append(i)
            break
        if visited.get(idx):
            break
        else:
            visited[idx] = 1
        temp = str(tmp)
ans.sort()
for i in ans:
    print(i)
