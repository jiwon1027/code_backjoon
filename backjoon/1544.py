n = int(input())

word = []
for _ in range(n):
    word.append(input())

from collections import deque

for i in word:
    queue = deque(i)
    while True:
        queue.append(queue.popleft())
        temp = ''. join(queue)
        if temp == i:
            break
        if temp in word:
            num = word.index(temp)
            word.pop(num)
            print(word)
#print(word)
print(len(set(word)))

