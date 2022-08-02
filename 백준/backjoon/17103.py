import sys
input = sys.stdin.readline

def isPrime(num):
    prime = [True]*num

    for i in range(2,int(num**0.5)+1):
        if prime[i]:
            for j in range(2*i,num,i):
                prime[j] = False
    return prime

prime_list = isPrime(1000000)
for _ in range(int(input())):
    n = int(input())
    cnt = 0
    for i in range(2,(n//2)+1):
        if prime_list[i] and  prime_list[n-i]:
            cnt += 1
    print(cnt)