import sys
input = sys.stdin.readline
n = int(input())
s = set()

for _ in range(n):
    temp = input().strip().split()


    if len(temp) == 1:
        if temp[0] == 'all':
            s = set([i for i in range(1, 21)])
        else:
            s = set()
    else:
        command, data = temp[0], temp[1]
        data = int(data)

        if command == 'add':
            s.add(data)
        elif command == 'remove':
            s.remove(data)
        elif command == 'check':
            if data in s:
                print(1)
            else:
                print(0)
        elif command == 'toggle':
            if data in s:
                s.discard(data)
            else:
                s.add(data)



