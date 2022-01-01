alpabat = [0] * 26

data = list(input())
for i in data:
    alpabat[ord(i)-97] +=1

for i in alpabat:
    print(i,end=' ')