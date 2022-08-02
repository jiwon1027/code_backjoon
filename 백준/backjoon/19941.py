n, k = map(int, input().split())
data = list(input())
res = 0
for idx in range(n):
    if data[idx] == 'P':
        for i in range(max(idx-k, 0), min(idx+k+1, n)):
            if data[i] == 'H':
                data[i] = 0
                res += 1
                break
#print(data)
print(res)