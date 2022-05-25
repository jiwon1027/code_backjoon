from itertools import permutations
n,k = 50,2
temp = [0] * (n-k) + [1] * k

data = set()
res = []
for i in permutations(temp):
    print(i)
'''
for i in data:
    value = ''
    print(i)
    for j in i:
        value += str(j)
    res.append(value)
print(res)
answer = 0
for i in res:
    if int(i,2) % 3 == 0:
        answer += 1
print()
'''


