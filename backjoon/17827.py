import sys
input = sys.stdin.readline

n,m,v = list(map(int,input().split()))

node = list(map(int,input().split()))
temp = node[v-1:]

for _ in range(m):
    question = int(input())
    if question < n:
        print(node[question])
    else:
        question = question - n
        question = question % (n-v+1)

        print(temp[question])

