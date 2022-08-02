import sys

n = int(sys.stdin.readline())
queue = []

for _ in range(n):
    command = sys.stdin.readline().split()

    if command[0] == 'push':
        queue.insert(0, command[1])
    elif command[0] == 'size':
        print(len(queue))
    elif command[0] == 'pop':
        if queue == []:
            print(-1)
        else:
            print(queue.pop())
    elif command[0] == 'empty':
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    elif command[0] == 'front':
        if queue == []:
            print(-1)
        else:
            print(queue[len(queue)-1])
    elif command[0] == 'back':
        if queue == []:
            print(-1)
        else:
            print(queue[0])

