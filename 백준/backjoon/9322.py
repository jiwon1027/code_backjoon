import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    first_public_key = input().split()
    second_public_key = input().split()
    cyphertext = input().split()
    for i in first_public_key:
        print(cyphertext[second_public_key.index(i)],end=' ')
    print()