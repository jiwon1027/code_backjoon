n = int(input())
num = 0
'''
for i in range(n + 1, n ** 2, n + 1):
    num += i
'''
for i in range(1,n):
    num += (n*i + i)

print(num)


