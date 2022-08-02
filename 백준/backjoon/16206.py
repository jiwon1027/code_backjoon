n,m = list(map(int,input().split()))
data = list(map(int,input().split()))
data.sort(key=lambda x:(x%10,x))
res = 0
#print(data)
for temp in data:
    cnt = temp//10
    if temp % 10: #나머지가 있을 때
        if cnt <= m:
            res += cnt
            m -= cnt
        else:
            res += m
            m -= m
    else: # 나머지가 없을 때
        if cnt-1 <= m:
            res += cnt
            m -= cnt-1
        else:
            res += m
            m -= m
    #print(res,m)
print(res)


