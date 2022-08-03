#2진수 바로 바꾸는 메소드 쓰거나 직접 구현하는 방법

# def dfs(x):
#     if x == 0:
#         return
#     else:
#         dfs(x//2)
#         print(x%2, end='')
#
# n = int(input())
# dfs(n)

print(bin(int(input()))[2:])