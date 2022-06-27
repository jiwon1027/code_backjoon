import math
for _ in range(int(input())):
    S, N, T, L = input().split()
    bigO = 0
    N,T,L = int(N),int(T),int(L)
    flag = False

    if S == 'O(N)':
        bigO = N * T
    elif S == 'O(N^2)':
        bigO = (N ** 2) * T
    elif S == 'O(N^3)':
        bigO = (N ** 3) * T
    elif S == 'O(2^N)':
        bigO = (2 ** N) * T
    elif S == 'O(N!)':
        bigO = math.factorial(N)*T

    if (10 ** 8) * L < bigO:
        print('TLE!')
    else:
        print('May Pass.')
