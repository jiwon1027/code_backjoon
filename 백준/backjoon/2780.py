for _ in range(int(input())):
    n = int(input())
    dp = [1] * 10
    for _ in range(n-1):
        temp = dp.copy()

        dp[0] = temp[7]
        dp[1] = temp[2] + temp[4]
        dp[2] = temp[1] + temp[3] + temp[5]
        dp[3] = temp[2] + temp[6]
        dp[4] = temp[1] + temp[5] + temp[7]
        dp[5] = temp[2] + temp[4] + temp[6] + temp[8]
        dp[6] = temp[3] + temp[5] + temp[9]
        dp[7] = temp[4] + temp[8] + temp[0]
        dp[8] = temp[5] + temp[7] + temp[9]
        dp[9] = temp[6] + temp[8]
    print(sum(dp)%1234567)
