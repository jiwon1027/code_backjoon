n = int(input())

temp = list(map(int, input().split()))
std = temp[0]
data = temp[1:]

data.sort()

for i in data:
    if std > i:
        std += i
    else:
        print('No')
        exit()
print('Yes')