t = int(input())
for k in range(t):
    n = int(input())
    data = list(map(int,input().split()))
    temp = []
    for i in data:
        if i % 2 == 1:
            temp.append(0)
        else:
            temp.append(1)

    if n == 1:
        print('#' + str(k + 1), end=' ')
        print(0)
    else:
        if temp.count(0) != temp.count(1):
            print('#' + str(k + 1), end=' ')
            print(-1)
        else:
            res = 10000
            for std in range(2):
                cnt = 0
                ans = []
                if n%2 == 1:
                    ans = [0,1] * ((n-1)//2) + [0]
                else:
                    ans = [0,1] * (n//2)

                while True:
                    if temp == ans:
                        break
                    for i in range(n-1):
                        if i%2==0:
                            if temp[i] == 1 and temp[i+1] == 0:
                                temp[i] = 0
                                temp[i+1] = 1
                                cnt += 1
                        else:
                            if temp[i] == 0 and temp[i+1] == 1:
                                temp[i] = 1
                                temp[i+1] = 0
                                cnt += 1
            res = min(res,cnt)
            print(res)



