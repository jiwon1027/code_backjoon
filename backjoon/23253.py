import sys
input = sys.stdin.readline

n,m = list(map(int,input().split()))

for _ in range(m):
    k = int(input())
    data = list(map(int,input().split()))

    if not data == sorted(data,reverse=True):
        print("No")
        exit()
print("Yes")




