x,y = input().split()

x = int(x[::-1])
y = int(y[::-1])


res = x+y
print(int(str(res)[::-1]))
