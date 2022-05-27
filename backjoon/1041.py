n = int(input())
data = list(map(int,input().split()))

#제일 윗면 :  3면*4 + 2면*(n-2)*4 + 1면*(n**2 - (n-2)*4 - 4)
#나머지면 : 2면*4 + 1면*(n-2)*4

a = min(data[0],data[5])
b = min(data[1],data[4])
c = min(data[2],data[3])

three = a+b+c
two = min(a+b, a+c, b+c)
one = min(a,b,c)

if n == 1:
    print(sum(data) - max(data))
else:
    top = three*4 + two*(n-2)*4 + one*(n**2 - (n-2)*4 - 4)
    middle = (two*4 + one*(n-2)*4) * (n-1)

    print(top+middle)

