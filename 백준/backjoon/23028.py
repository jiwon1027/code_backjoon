n, a, b = list(map(int,input().split()))

x = [0] * 10
y = [0] * 10
tempA = 0
tempB = 0
for i in range(10):
    x[i],y[i] = list(map(int,input().split()))

    if a >=66 and b>= 130:
        print("Nice")
    else:
        for i in range(8-n):
            for j in range(x[i]+ y[i]):
                if j == 6:
                    break
                elif j >= x[i]:
                    tempB += 3
                else:
                    tempA += 3


        a = a + tempA + tempB
        b = b + tempA + tempB
        #print(a, b)
        if a >= 66 and b >= 130:
            print("Nice")
            break
        else:
            print("Nae ga wae")
            break