import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
data = list(map(int,input().split()))
data.sort()

left = 0
right = n-1
res = 0
while True:
    if left >= right:
        break

    if data[left] + data[right] == m:
        res += 1
        left += 1
        right -= 1
    elif data[left] + data[right] > m:
        right -= 1
    else:
        left += 1
print(res)