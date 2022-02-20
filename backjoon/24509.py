n = int(input())
student = []
res = []
for _ in range(n):
    student.append(list(map(int, input().split())))

student.sort(key = lambda x : (-x[1], x[0]))
res.append(student[0][0])

student.sort(key = lambda x : (-x[2], x[0]))
for i in range(n):
    if not student[i][0] in res:
        res.append(student[i][0])
        break


student.sort(key = lambda x : (-x[3], x[0]))
for i in range(n):
    if not student[i][0] in res:
        res.append(student[i][0])
        break


student.sort(key = lambda x : (-x[4], x[0]))
for i in range(n):
    if not student[i][0] in res:
        res.append(student[i][0])
        break

print(*res)
