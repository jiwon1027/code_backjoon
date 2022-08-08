for tc in range(int(input())):
    n,m = list(map(int,input().split()))
    data = list(map(int,input().split()))
    data.sort(reverse=True)


    res = 0

    for x in data[:n-1]:
        for y in data[1:]:
            temp = x+y
            if temp <= m and res < temp:
                res = temp
    if res == 0:
        print('#',tc," ",-1)
    else:
        print('#',tc," ",res)



