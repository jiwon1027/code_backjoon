data = [1,1,2,4] + [0]*64
for i in range(4,68):
    data[i] = data[i-1] + data[i-2] + data[i-3] + data[i-4]

for _ in range(int(input())):
    n = int(input())
    print(data[n])


