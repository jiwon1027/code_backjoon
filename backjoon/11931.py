import sys
input = sys.stdin.readline

n = int(input().rstrip())
data = []
for _ in range(n):
    data.append(int(input().rstrip()))
data.sort(reverse=True)

for i in data:
    print(i)