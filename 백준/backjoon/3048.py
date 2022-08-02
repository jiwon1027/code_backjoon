n1, n2 = list(map(int,input().split()))
data1 = list(input())
data2 = list(input())
t = int(input())

data1.reverse()

# N1 N2 통합
N_sum = data1 + data2

for t in range(t):
    # swap해야하는 idx 값 저장
    temp = []

    for q in range(1, len(N_sum)):

        # 왼쪽 방향으로 이동하는 경우만 확인하면 됨
        # <- -> 의 경우는 방향이 서로 달라도 swap할 필요 없음
        if N_sum[q] in data2:
            if N_sum[q - 1] in data1:
                temp.append(q)

    # swap 해주기
    for w in temp:
        N_sum[w], N_sum[w - 1] = N_sum[w - 1], N_sum[w]

res = ''

for r in N_sum:
    res += r

print(res)


