import sys
input = sys.stdin.readline

n = int(input())
hash = {}

for _ in range(n):
    name, log = input().split()

    if log == 'enter':
        hash[name] = 1
    else:
        hash[name] = 0

res = []
for key,value in hash.items():
    if value:
        res.append(key)

res.sort(reverse=True)

for i in res:
    print(i)