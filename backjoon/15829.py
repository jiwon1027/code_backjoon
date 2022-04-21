n = int(input())
data = input()

res = 0
for i in range(len(data)):
    temp = ord(data[i]) - 96
    #print(temp)
    res += temp * (31 ** i)
print(res % 1234567891)

