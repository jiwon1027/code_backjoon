import sys
input = sys.stdin.readline
n,m = list(map(int,input().split()))

dict = {}

for _ in range(n):
    address, pwd = input().split()
    dict[address] = pwd

for _ in range(m):
    temp = input().rstrip()
    print(dict.get(temp))

