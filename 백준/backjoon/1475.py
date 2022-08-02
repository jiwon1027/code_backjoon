n = input()
data = [0] * 10
for i in n:
    i = int(i)
    if i == 6 or i == 9:
        if data[6] >= data[9]:
            data[9] += 1
        else:
            data[6] += 1
    else:
        data[i] += 1
print(max(data))