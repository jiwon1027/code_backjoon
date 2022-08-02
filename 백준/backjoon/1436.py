n = int(input())

cnt = 0
str_666 = 666

while True:
    if '666' in str(str_666):
        cnt += 1
    if cnt == n:
        print(str_666)
        break
    str_666 += 1
