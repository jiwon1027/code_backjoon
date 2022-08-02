from collections import deque
import sys


t = int(input())
for _ in range(t):
    data = sys.stdin.readline().rstrip()
    n = int(input())
    arr = deque(sys.stdin.readline().rstrip()[1:-1].split(','))
    #print(arr)

    if n == 0:
        arr = deque()

    R_cnt = 0

    for i in data:
        if i == 'R':
            R_cnt += 1
        elif i == 'D':
            try:
                if R_cnt % 2:
                    arr.pop()
                else:
                    arr.popleft()
            except:
                print('error')
                break
    else:
        if R_cnt % 2:
            arr.reverse()
            print('[' + ','.join(arr) + ']')
        else:
            print('[' + ','.join(arr) + ']')



