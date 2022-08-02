from fractions import Fraction
import sys
input = sys.stdin.readline

n,m = list(map(int,input().split()))
drink = []
#idx, total, sugar
for _ in range(n):
    w,v = list(map(int,input().split()))
    drink.append((w,v))

drink.sort(key=lambda x : -(x[1]/x[0]))

remain_sugar = m
ans = []
a,b = 0,0
for L,sugar in drink:

    if remain_sugar - L <= 0:
        b = L
        a = sugar*remain_sugar
        ans.append(Fraction(a,b))
        break
    else:
        remain_sugar = m - L
        b = L
        a = remain_sugar * sugar
        ans.append(Fraction(a,b))

#print(ans)
if sum(ans) % 1:
    print(sum(ans))
else:
    print('{}/{}'.format(sum(ans),1))



