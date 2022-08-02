a, b = list(map(int,input().split()))
alist = list(map(int,input().split()))
blist = list(map(int,input().split()))

aset = set(alist)
bset = set(blist)


temp = aset - bset
temp1 = bset - aset


print(len(temp) + len(temp1))
