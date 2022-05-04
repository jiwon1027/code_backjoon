n = int(input())
m = int(input())
s = input()

pn = ''
for i in range(n):
    pn += 'I'
    pn += 'O'
pn += 'I'

cnt = 0
for i in range(m - len(pn) + 1):
    #print(i)
    if s[i] == 'I':
        if s[i:i+len(pn)] == pn:
            cnt += 1
print(cnt)
