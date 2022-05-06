def func_D(data):
    data = 2 * data
    if data > 9999:
        data %= 10000
    return data

def func_S(data):
    if not data:
        return 9999
    else:
        return data-1

def func_L(data):
    data = str(data)
    data = data[1:] + data[0]
    return data

def func_R(data):
    data = str(data)[-1::-1]
    return data

from collections import deque
def search(A):
    queue = deque()
    queue.append((A,''))
    visited = [False] * 10000
    visited[A] = True

    while queue:
        num, command = queue.popleft()
        if num == B:
            print(command)
            return
        temp = func_D(num)
        if not visited[temp]:
            visited[temp] = 1
            queue.append((temp,command+'D'))

        temp = func_S(num)
        if not visited[temp]:
            visited[temp] = 1
            queue.append((temp,command+'S'))

        temp = func_L(num)
        if not visited[temp]:
            visited[temp] = 1
            queue.append((temp,command+'L'))

        temp = func_R(num)
        if not visited[temp]:
            visited[temp] = 1
            queue.append((temp,command+'R'))

import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    A, B = list(map(int,input().split()))
    search(A)

