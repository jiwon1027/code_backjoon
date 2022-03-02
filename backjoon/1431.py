def sum_number(str):
    res = 0
    for i in str:
        if i.isdigit():
            res += int(i)
    return res

n = int(input())
data = []

for _ in range(n):
    temp = input()
    data.append(temp)

data.sort(key=lambda x : (len(x), sum_number(x), x))
for i in range(n):
    print(data[i])

