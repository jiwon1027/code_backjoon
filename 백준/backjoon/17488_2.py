n,m = list(map(int,input().split()))
limit_stu = list(map(int,input().split()))
temp = limit_stu[:]
sugang = [[0] * m for _ in range(n)]

for i in range(n):
    first_surang = list(map(int,input().split()))
    if not len(first_surang) == 1:
        for j in range(len(first_surang)-1):
            sugang[i][first_surang[j]-1] = 1
            temp[i] = temp[i] - temp[first_surang[i]-1]

for i in range(n):
    second_surang = list(map(int,input().split()))
    if not len(second_surang) == 1:
        for j in range(len(second_surang) - 1):
            sugang[i][second_surang[j] - 1] = 1
            temp[i] = temp[i] - temp[second_surang[i] - 1]

print(limit_stu)
print(temp)
print(sugang)