while True:
    cnt = 0
    data = list(map(int,input().split()))
    #print(data[:-1])
    if data == [-1]:
        break
    for i in data[:-1]:
        if i*2 in data[:-1]:
            #print(i)
            cnt += 1
    print(cnt)



