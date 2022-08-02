n,k = list(map(int,input().split()))
data = []
for i in range(1,n+1):
    data.append(list(map(int,input().split())))
data.sort(key=lambda x : (-x[1],-x[2],-x[3]))
#올림픽이니까 금은동순으로 내림차순 정렬 해줄필요가 있었음
#재밌는점은 동점이 나오면 공등2등이고 그 다음 등수는 3등이 없는 4등이 된다는 것인데
#이건 일일이 구현으로 해줌
#먼저 내가 구할 k나라의 index를 구해준다음에
#index를 기준으로 잡고 나머지 for문 쫙 돌리면서 금은동 개수가 똑같다? 그럼 그때 i+1을 해주면됨
#why? i는 0부터 시작하니까
idx = 0
for i in range(n):
    if data[i][0] == k:
        idx = i
for i in range(n):
    if data[idx][1:] == data[i][1:]:
        print(i+1)
        break

