import sys
input = sys.stdin.readline
# 단순히 3가지 규칙에 대해서 정렬 해주면 되는 문제임
# 1초의 시간제한 때문에 dict()을 써서 저장해주고 sort()
n,m = list(map(int,input().split()))
data = dict()
for _ in range(n):
    temp = input().strip()
    if len(temp) >= m:
        if data.get(temp):
            data[temp] += 1
        else:
            data[temp] = 1
res = sorted(data.items(),key=lambda x:(-x[1],-len(x[0]),x[0]))
for word,i in res:
    print(word)
