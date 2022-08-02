x, y = list(map(int,input().split()))

weekend = ['MON','TUE','WED','THU','FRI','SAT','SUN']

res = 0

day_31 = [1,3,5,7,8,10,12]
day_30 = [4,6,7,9,11]

for i in range(1,x):
    if i in day_31:
        res += 31
    elif i in day_30:
        res += 30
    else:
        res += 28
res += y
print(weekend[(res % 7) - 1])