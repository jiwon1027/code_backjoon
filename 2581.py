m = int(input())
n = int(input())

list = []               #소수
for x in range(m,n+1):  #1부터 자기자신까지 반복시키면서 나누어떨어지는 값이 있는지 찾는다.
    sosucnt = 0
    for i in range(1,x+1):
        if x % i == 0:
            sosucnt += 1
    if sosucnt == 2:
        list.append(int(x))

if sum(list)==0:
    print(-1)
else:
    print(sum(list))
    print(list[0])