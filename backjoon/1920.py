#in 사용

import sys
input = sys.stdin.readline

n = int(input())
a_list = list(map(int, input().split()))
m = int(input())
m_list = list(map(int, input().split()))

for i in m_list:
    if i in a_list:
        print(1)
    else:
        print(0)