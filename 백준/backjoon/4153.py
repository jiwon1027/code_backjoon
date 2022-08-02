while True:
    data = list(map(int,input().split()))
    if data.count(0)==3:
        break
    max_temp = max(data)
    data.remove(max_temp)
    temp=data[0]*data[0] + data[1]*data[1]

    if temp == max_temp*max_temp:
        print('right')
    else:
        print('wrong')
