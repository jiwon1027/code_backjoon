data = []
for i in range(5):
    temp = int(input())
    if temp < 40:
        data.append(40)
    else:
        data.append(temp)
print(int(sum(data)/5))