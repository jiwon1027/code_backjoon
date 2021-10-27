cnt = 0
data = []
while True:
    n = int(input('정수를 입력하시오 :'))
    if n == -99:
        break
    data.append(n)
    cnt += 1

print(f'{cnt}개의 유효한 정수중 가장 큰 정수는 {max(data)} 이고, 가장 작은 정수는 {min(data)}이다. ')