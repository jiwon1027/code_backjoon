n = int(input())
result = 0
#n이 50000까지라서 모든 구간을 스레드같이 돌린다는 생각은 안됨
#그럼 시간 증가시키면서 고려하는 방법 밖에 없는듯

for i in range(n):
    a,b = map(int,input().split())

    if i == 0:
        result += b
    else:
        while True:
            result += 1
            if result % (a+b) >= b:
                break

print(result+1)
