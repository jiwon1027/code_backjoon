m, n = list(map(int, input().split()))
num_alphbet = ['zero','one','two','three','four','five','six','seven','eight','nine']
data = []
for i in range(m,n+1):
    if i > 9:
        data.append([i,num_alphbet[i//10] + num_alphbet[i%10]])
    else:
        data.append([i,num_alphbet[i]])
data.sort(key=lambda x : x[1])

for i in range(len(data)):
    if i % 10 == 0 and i != 0:
        print()
    print(data[i][0], end=' ')
