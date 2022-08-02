#이분 탐색

import sys
input = sys.stdin.readline

n = int(input())
a_list = list(map(int, input().split()))

a_list.sort()

m = int(input())
m_list = list(map(int, input().split()))

def binary_search(array, target, start, end):
    if start > end:
        return 0
    mid = (start + end) // 2
    if array[mid] == target:
        return 1
    elif array[mid] > target:
        return binary_search(array, target, start, mid - 1)
    elif array[mid] < target:
        return binary_search(array, target, mid + 1, end)
for i in m_list:
    print(binary_search(a_list,i,0,n-1))
