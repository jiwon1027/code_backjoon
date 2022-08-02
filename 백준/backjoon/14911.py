from itertools import combinations

data = sorted(map(int, input().split()))
n = int(input())

cnt = 0
ans = []
for i in combinations(data, 2):
    if sum(i) == n and [i[0], i[1]] not in ans:
        ans.append([i[0], i[1]])
        cnt += 1

for i in range(cnt):
    print(ans[i][0], ans[i][1])
print(cnt)