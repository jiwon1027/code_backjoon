n,x = list(map(int,input().split()))
visiter = list(map(int,input().split()))

sum_value = sum(visiter[:x])
max_value = sum_value

res = 1
#x일만큼 슬라이드 하면서 봐야하니까 슬라이드 윈도우 문제임
#이중 반복문을 피하기 위해 다음 슬라이드는 현재 슬라이드에서 제일 앞에껄 빼고
#슬라이드해서 새로 만나는 부분을 더해주면 이게 다음슬라이드의 정보가 됨
#이걸 이용해서 max값을 계속 갱신해가고 만약 값이 똑같다면 day+=1해주면서 기간을 늘림
for i in range(n-x):
    sum_value -= visiter[i]
    sum_value += visiter[i+x]
    if sum_value > max_value:
        res = 1
        max_value = sum_value
    elif sum_value == max_value:
        res += 1

if sum_value != 0:
    print(max_value)
    print(res)
else:
    print("SAD")

