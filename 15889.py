n = int(input())
data = list(map(int,input().split()))
if not n == 1:
    data2 = list(map(int,input().split()))
max_value = 0

for i in range(n-1):
    #사거리 긴애가 던져야됨 똑같은 자리에 잇으면
    max_value = max(max_value, data[i]+data2[i])
    if max_value >= data[i+1]:
        continue
    else:
        print('엄마 나 전역 늦어질 것 같아')
        exit()
print('권병장님, 중대장님이 찾으십니다')
