n = int(input())
data = []

for i in range(n):
    start_time, end_time = map(int,input().split())
    data.append([start_time,end_time])

data.sort(key=lambda x: (x[1], x[0]))

last = 0
conut = 0

for i, j in data:
  if i >= last:
    conut += 1
    last = j

print(conut)