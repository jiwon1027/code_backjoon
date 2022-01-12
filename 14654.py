n = int(input())
a = 0
b = 0
ans = 0
before = 0

aTeam = list(map(int,input().split()))
bTeam = list(map(int,input().split()))

def result(a,b):
    if a == 3 and b == 1:
        return -1
    elif a == 1 and b == 3:
        return 1
    elif a < b:
        return -1
    elif a > b:
        return 1
    else:
        return 0

for i in range(n):
    temp = result(aTeam[i],bTeam[i])

    if temp == 1:
        a += 1
        ans = max(ans, max(a,b))
        b = 0
        before = 1

    elif temp == -1:
        b += 1
        ans = max(ans, max(a,b))
        a = 0
        before = -1

    else: #비겼을때
        if before == 1:
            b += 1
            ans = max(ans, max(a, b))
            a = 0
            before = -1
        else:
            a += 1
            ans = max(ans, max(a, b))
            b = 0
            before = 1
print(ans)
