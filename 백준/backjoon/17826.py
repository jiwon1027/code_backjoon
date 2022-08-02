data = list(map(int,input().split()))
n = int(input())
data.append(n)

data.sort(reverse=True)
result = data.index(n) + 1


if 1 <= result <= 5:
    print('A+')
elif 6 <= result <= 15:
    print('A0')
elif 16 <= result <= 30:
    print('B+')
elif 31 <= result <= 35:
    print('B0')
elif 36 <= result <= 45:
    print('C+')
elif 46 <= result <= 48:
    print('C0')
elif 49 <= result <= 50:
    print('F')
