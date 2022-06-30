import sys
input = sys.stdin.readline

def check_prime(x):
    for i in range(2,int(x**0.5)+1) :
        if x % i == 0 :
            return 1 # 합성수
    return 0 # 아니다!

for _ in range(int(input())) :
    K = int(input())
    if check_prime(K) == 0 :
        print(0)
    else :
        start = K
        end = K
        while True :
            if check_prime(start) == 0 :
                break
            else :
                start -= 1
        while True :
            if check_prime(end) == 0 :
                break
            else :
                end += 1
        print(end - start)
