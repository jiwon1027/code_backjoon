import math

def f_lcm(data): #재귀함수로 표현하고싶었는데 어떻게 할지 잘 몰랐음
    temp = data[0]
    for i in range(len(data) - 1):
        if temp != 0 and data[i+1] != 0: #0은 최소공배수를 구하는것에 빠지는 조건
            temp = temp * data[i+1] // math.gcd(temp, data[i+1])
    return temp

def recursive_lcm(a,b,idx): # 재귀로 해보려고 했는데 못하겠다ㅠㅠ
    global lcm
    print(a,b,idx,lcm)
    if idx == len(data):
        return
    if a != 0 and b != 0:
        lcm = a * b // math.gcd(a, b)
        recursive_lcm(lcm, data[idx],idx+1)

#n = input()
n = '1000000000'
data = list()
for i in n:
    data.append(int(i))
lcm = f_lcm(data)

#lcm = 0
#recursive_lcm(data[0],data[1],2)
#print(lcm)

if int(n) % lcm == 0:
    print(n)
else:
    n += '0'
    flag = 1
    while True:
        for i in range(int(n), int(n) + (10**flag)):
            if i % lcm == 0:
                print(i)
                exit()
        else:
            n += '0'
            flag += 1




