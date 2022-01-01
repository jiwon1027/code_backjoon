import sys
n = 1000000
dp = [True] * n
for i in range(2, int(n ** 0.5) + 1):
    if dp[i]:
        for j in range(2 * i, n, i):
            dp[j] = False


while True: #list에서 in을 사용할 경우 시간복잡도가 O(n)
    n = int(sys.stdin.readline())
    if n == 0: #끝내기
        break

    temp = False
    for i in range(3, n):
        if dp[i] == True:
            if dp[n - i] == True:
                print("%d = %d + %d" % (n, i, n - i))
                temp = True
                break

    if temp == False:
        print("Goldbach's conjecture is wrong.")
