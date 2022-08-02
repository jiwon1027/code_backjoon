n,t = list(map(float,input().split()))
x = list(map(int,input().split()))
v = list(map(int,input().split()))

min_value = 0
max_value = float('inf')


for i in range(int(n)): #학생 수 만큼 돌려

    left = round(x[i] - v[i] * t,4) #반올림 why ) 실수 오류 때문에 in python
    right = round(x[i] + v[i] * t,4)

    if max_value < left or right < min_value:
        print(0)
        exit()
    max_value = min(max_value,right)
    min_value = max(min_value,left)

print(1)


