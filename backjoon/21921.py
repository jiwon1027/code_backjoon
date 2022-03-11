n,x = list(map(int,input().split()))
visiter = list(map(int,input().split()))

sum_value = sum(visiter[:x])
max_value = sum_value

res = 1

for i in range(n-x):
    print(i)
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