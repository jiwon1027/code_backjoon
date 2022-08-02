#순열을 이용한 완전 탐색 방법
from itertools import permutations
import math

r,c = map(int,input().split())
person = [list(map(int, input().split())) for _ in range(3)]

ans = float('inf')
yummi = [r,c]


def cal(a,b):
    return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)


for i in permutations(person):
    print(i)
    temp = 0
    present = yummi
    for p in i:
        next = p
        temp += cal(present,next)
        present = p

    ans = min(ans,temp)

print(int(ans))
