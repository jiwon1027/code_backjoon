import sys

stack1 = list(sys.stdin.readline().strip())
stack2 = []
n = int(sys.stdin.readline())
cursor = len(stack1)

for _ in range(n):
    x = sys.stdin.readline().split()

    if x[0] == 'L' and stack1 != []:
        stack2.append(stack1.pop())

    elif x[0] == 'D' and stack2 != []:
        stack1.append(stack2.pop())

    elif x[0] == 'B' and stack1 != []:
        stack1.pop()

    elif x[0] == 'P':
        stack1.append(x[1])

print(''.join(stack1 + list(reversed(stack2))))


