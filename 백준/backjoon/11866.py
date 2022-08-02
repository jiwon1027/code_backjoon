from collections import deque
n, k = map(int,input().split())

queue = deque(list(range(1,n+1)))
result = []


while queue:
    for i in range(k-1):
        queue.append(queue.popleft())
    result.append(queue.popleft())

result = map(str,result)
print('<',end ='')
print(', '.join(result),end='')
print('>')
