n_test = int(input())

for _ in range(n_test):
    n,m = map(int,input().split())
    data = list(map(int,input().split()))
    dp = [0] * n
    dp[m] = 1

    order = 0

    while True:
        print(data)
        print(dp)
        if data[0] == max(data):
            order += 1

            if dp[0] == 1: #중복으로 1111계속 나오는데 그 값이 맞는지 확인 하기 위해
                print(order)
                break
            else:
                data.pop(0)
                dp.pop(0)

        elif data[0] < max(data):
            data.append(data.pop(0))
            dp.append(dp.pop(0))
