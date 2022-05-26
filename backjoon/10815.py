n = int(input())
data = list(map(int,input().split()))

m = int(input())
card = list(map(int,input().split()))

data.sort()

from bisect import bisect_left,bisect_right
for i in card:
    left = bisect_left(data,i)
    right = bisect_right(data,i)

    if left == right:
        print(0, end=' ')
    else:
        print(1, end=' ')

'''
n = int(input())
data = set(map(int,input().split()))

m = int(input())
card = list(map(int,input().split()))


for i in card:
    if i in data:
        print(1, end=' ')
    else:
        print(0, end=' ')
'''