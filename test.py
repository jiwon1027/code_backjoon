n = 20
for i in range(1, int(n**0.5)):
    if n % i == 0:
        print(i, end=" ")
        print(n//i, end=" ")
i += 1
if i**2 == n:
    print(i)

