import sys
input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))
stack = []
answer = [-1 for i in range(n)]

for i in range(len(data)):
    while stack and data[stack[-1]] < data[i]:
        answer[stack.pop()] = data[i]
    stack.append(i)
print(*answer)