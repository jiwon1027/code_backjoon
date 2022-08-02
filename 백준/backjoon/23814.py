d = int(input())
n,m,k = list(map(int,input().split()))

total = n+m+k
max_mandu = total // d
remainder1 = n % d
remainder2 = m % d

mandu = [0] * 4
k_list = [0] * 4
mandu[0] = n//d + m//d + k//d
k_list[0] = k

mandu[1] = (n+(d-remainder1))//d + m//d + (k-(d-remainder1))//d
k_list[1] = (k-(d-remainder1))

mandu[2] = n//d + (m+(d-remainder2))//d + (k-(d-remainder2))//d
k_list[2] = (k-(d-remainder2))

mandu[3] = (n+(d-remainder1))//d  + (m+(d-remainder2))//d + (k-(d-remainder1) - (d-remainder2))//d
k_list[3] = (k-(d-remainder1) - (d-remainder2))

res = 0
for idx, value in enumerate(mandu):
    if value == max_mandu:
        res = max(k_list[idx],res)

print(res)