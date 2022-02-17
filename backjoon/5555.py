data = input()
n = int(input())


res = 0
for _ in range(n):
    temp = input()
    temp += temp
    if temp.find(data) != -1:
        res += 1
print(res)