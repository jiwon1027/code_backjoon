import sys
while True:
    temp = list(sys.stdin.readline())
    if not temp:
        break
    s, u, n, b = 0,0,0,0
    for i in temp:
        if i == ' ':
            b += 1
        elif ord(i) >= 48 and ord(i) <= 57:
            n+= 1
        elif ord(i) >= 65 and ord(i) <= 90:
            u += 1
        elif ord(i) >= 97 and ord(i) <= 122:
            s += 1
    print(s, u, n, b)