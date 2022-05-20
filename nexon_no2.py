n = int(input())
c = []
for _ in range(n):
    c.append(input())
n = int(input())
x = []
for _ in range(n):
    x.append(int(input()))
n = int(input())
y = []
for _ in range(n):
    y.append(int(input()))
m = int(input())
q = []
for _ in range(n):
    q.append(input())
print(c)
print(x)
print(y)
print(q)

'''
for i in range(n):
    idx, temp = i, 10**9
    for j in range(n):
        
        if x[i] == x[j] and abs(y[i] - y[j]):
            if temp > abs(y[i] - y[j]):
                idx = j
                temp = abs(y[i] - y[j])
            elif temp == abs(y[i] - y[j]):
                if c[idx] > c[j]:
                    idx = j

        if y[i] == y[j] and abs(x[i] - x[j]):
            if temp > abs(x[i] - x[j]):
                idx = j
                temp = abs(x[i] - x[j])
            elif temp == abs(x[i] - x[j]):
                if c[idx] > c[j]:
                    idx = j

    if idx == i:
        print('NONE')
    else:
        print(c[idx])
'''
#브루트포스
res = []
for name in q:
    idx = c.index(name) #기준
    index, temp = idx, 10 ** 9
    for i in range(n):
        if idx != i:
            if x[i] == x[idx]:
                if temp > abs(y[i]-y[idx]):
                    index = i
                    temp = abs(y[i]-y[idx])

                elif temp == abs(y[i] - y[idx]):
                    if c[index] > c[i]:
                        index = i

            if y[i] == y[idx]:
                if temp > abs(x[i]-x[idx]):
                    index = i
                    temp = abs(x[i]-x[idx])

                elif temp == abs(x[i] - x[idx]):
                    if c[index] > c[i]:
                        index = i
    if index == idx:
        print('NONE')
    else:
        print(c[index])




