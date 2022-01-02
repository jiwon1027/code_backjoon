n,m = list(map(int,input().split()))
limit_stu = list(map(int,input().split()))

for _ in range(n):
    first_surang = list(map(int,input().split()))
    if not len(first_surang) == 1:
        for i in range(len(first_surang)):
            limit_stu[i] = limit_stu[i] - first_surang[i]

print(limit_stu)


