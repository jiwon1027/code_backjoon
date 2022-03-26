import sys
input = sys.stdin.readline

N, L = list(map(int,input().split()))
data = list(map(int,input().split()))
data.sort()

tape = 1
start = data[0]
end = start + L - 0.5
for i in data:
    if end >= i:
        continue
    else:
        tape += 1
        end = i + L - 0.5
print(tape)

