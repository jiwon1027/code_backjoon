import sys
n=sys.stdin.readline()
a=sys.stdin.readline().split()
b=sys.stdin.readline().split()
m=int(sys.stdin.readline())
c=sys.stdin.readline().split()
for i in range(len(a))[::-1]:
    if a[i]=='1':
        del b[i]
res = b[::-1] + c
print(*res[:len(c)])
