data = []
def hanoi(N, start, to, via):
    if N == 1:
        data.append([start,to])
    else:
        hanoi(N-1, start, via, to)
        data.append([start,to])
        hanoi(N-1, via, to, start)


n = int(input())
hanoi(n, '1', '3', '2')

print(len(data))
for i in data:
    print(' '.join(i))