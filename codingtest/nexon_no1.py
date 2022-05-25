a = 1
b = 56
s = str(a // b) + "."
a %= b
hist = dict()
while True:
    a *= 10
    if a not in hist.keys():
        hist[a] = len(s)
        s += str(a // b)
        a %= b
    else:
        print(s[:hist[a]]  + s[hist[a]:len(s)], s[hist[a]:len(s)])
        break