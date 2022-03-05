money = 1000 - int(input())
b = [500, 100, 50, 10, 5, 1]
res = 0
for i in b:
    res += money // i
    money %= i
print(res)


'''

money = 1000 - int(input())

res = money // 500

res += (money % 500) // 100

res += ((money % 500) % 100) // 50

res += (((money % 500) % 100) % 50) // 10

res += ((((money % 500) % 100) % 50) % 10) // 5

res += ((((money % 500) % 100) % 50) % 10) % 5

print(res)
'''