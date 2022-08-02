broken = int(input())
n = int(input())
if broken == 1:
    print(5 + 8*(n-1) + 3)
elif broken == 5:
    print(5 + 8*(n-1) + 7)
else:

    if n % 2 == 1:
        print(5 + 4*(n-1) + (4-broken))
    else:
        print(5 + 4*(n-1) + (broken-2))