A, B, C = list(map(int,input().split()))
D = int(input())

C += D
B += C//60
A += B//60
print(A % 24,B % 60,C % 60)
