h1, m1, s1 = map(int, input().split(':'))
h2, m2, s2 = map(int, input().split(':'))
time = h2 * 3600 + m2 * 60 + s2 - (h1 * 3600 + m1 * 60 + s1)
if time < 0:
    time += 60 * 60 * 24
h = time // 3600
m = (time % 3600) // 60
s = time % 60

print("%02d:%02d:%02d" % (h,m,s))