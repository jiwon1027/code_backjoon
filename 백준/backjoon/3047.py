temp = list(map(int, input().split()))
data = input()

temp.sort()

for i in data:
    index = ord(i) - ord('A')
    print(temp[index], end=' ')