n = int(input())

round1 = list(map(int,input().split()))
round2 = list(map(int,input().split()))

result = sum(list(map(abs, round1))) + sum(list(map(abs, round2)))
print(result)