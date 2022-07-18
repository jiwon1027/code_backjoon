n = int(input('번호입력하세요 :'))
import random

win_cnt = 0
lose_cnt = 0
if n == 1:
    total = 5

    while total:
        temp = input()
        myinfor = -1
        if temp == '가위':
            myinfor = 1
        elif temp == '주먹':
            myinfor = 2
        elif temp == '보':
            myinfor = 3
        enemy = random.randint(1,4)

        if enemy == myinfor:
            print('비겼습니다')
        elif (myinfor==1 and enemy==3) or (myinfor==2 and enemy==1) or (myinfor==3 and enemy==2):
            print('이김')
            win_cnt +=1
        else:
            print('짐')
            lose_cnt +=1

        if win_cnt == 3 or lose_cnt == 3:
            break
        total -= 1
if win_cnt==lose_cnt:
    print('##비김')
elif win_cnt > lose_cnt:
    print('##이김')
else:
    print('##짐')

