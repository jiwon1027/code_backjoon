n,k,q = map(int,input().split())
x = 65
people = []
for i in range(n):
    people.append(chr(x+i))
check = [0] * 26
data = [[0,'']]
check[0] = 1
print(people)
for i in range(k):
    r,p = input().split()
    data.append([int(r),p])

print(data)
if data[q][0] == 0:
    print(-1)
    exit()

for i in range(1,k+1):
    if data[q][0] <= data[i][0]:
        check[people.index(data[i][1])] = 1
print(check)

for i in range(n):
    if not check[i]:
        print(people[i], end=' ')
