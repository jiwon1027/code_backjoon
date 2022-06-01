from datetime import datetime
import matplotlib.pyplot as plt


#시간이 0~24라는 범위에서 연산 후의 올바른 시간 return하는 함수
def cal_time(h,m): 
    if m < 0:
        m += 60
        h -= 1
    elif m > 59:
        m -= 60
        h += 1

    if h < 0:
        h += 24
    elif h > 23:
        h -= 24

    return h,m

# 결과를 출력하는 함수
def print_time(h,m):
    day = 'AM'

    if h >= 13:
        h -= 12
        day = 'PM'
    temp = f'{day} {h}:{m}'
    print(temp)


# sleep cycle 그리는 함수
def draw_graph(time_list,n):
    time_list[0] = i1,j1
    time_list[1] = i2,j2
    time_list[2] = i3,j3
    time_list[3] = i4,j4
    
    x = []
    x2 = []
    if n == '1': #n에 따라서 표시해야하는 x축의 범위가 다르기 때문에 x축 설정
        for i in range(h-11,h):
            if i >=24:
                x2.append(i-24)
            else:
                x.append(i)
    elif n == '2':
        for i in range(h, h + 11):
            if i >= 24:
                x2.append(i - 24)
            else:
                x.append(i)
    else:
        for i in range(h,h+13):
            if i >=24:
                x2.append(i-24)
            else:
                x.append(i)

    plt.subplot(121)
    plt.title('Sleep Cycle')
    plt.xlabel('Time of sleep')
    plt.ylabel('stage')
    plt.text(x[0], 4.5, 'Awake : Low voltage High frequency', fontsize=8)
    plt.text(x[0], 3.5, 'Stage1 : Low voltage Mixed frequency', fontsize=8)
    plt.text(x[0], 2.5, 'Stage2 : Sleep spindles & K complexes', fontsize=8)
    plt.text(x[0], 1.5, 'Stage3 : Mostly slow waves', fontsize=8)
    plt.text(x[0], 0.5, 'Stage4 : Slow waves', fontsize=8)

    plt.plot([(i1 + j1 // 60) - 0.25, (i1 + j1 // 60) + 0.25], [4, 4],'b-',label='REM')
    plt.plot([(i2 + j2 // 60) - 0.25, (i2 + j2 // 60) + 0.25], [4, 4],'b-')
    plt.plot([(i3 + j3 // 60) - 0.25, (i3 + j3 // 60) + 0.25], [4, 4],'b-')
    plt.plot([(i4 + j4 // 60) - 0.25, (i4 + j4 // 60) + 0.25], [4, 4],'b-')
    plt.legend()

    plt.xlim([x[0],x[-1]])
    plt.ylim([0, 5])

    if len(x2) > 0:
        plt.subplot(122)
        plt.xlabel('Time of sleep')
        plt.ylabel('stage')
        plt.plot([(i1 + j1 // 60) - 0.25, (i1 + j1 // 60) + 0.25], [4, 4], 'b-', label='REM')
        plt.plot([(i2 + j2 // 60) - 0.25, (i2 + j2 // 60) + 0.25], [4, 4], 'b-')
        plt.plot([(i3 + j3 // 60) - 0.25, (i3 + j3 // 60) + 0.25], [4, 4], 'b-')
        plt.plot([(i4 + j4 // 60) - 0.25, (i4 + j4 // 60) + 0.25], [4, 4], 'b-')
        plt.legend()

        plt.xlim([x2[0],x2[-1]])
        plt.ylim([0, 5])

    plt.show()


n = input('1.일어나야할 시간 입력 2.잠들시간 입력 3.현재 잠들 경우 : ')

# 입력받은 n이 '1','2','3'이 아니라면 반복해서 다시 입력을 받는 부분
while True:
    if n not in ['1','2','3']: 
        print('잘못된 입력입니다. 다시 입력해주세요')
        n = input('1. 일어나야할 시간 입력 2. 잠들시간 입력 3. 현재 잠들 경우 : ')
    else:
        break


if n == '1':
    while True:
        try: # 올바르지 않은 형식의 데이터들이 입력되면 예외처리를 이용하여 다시 입력을 받게 한다.
            day,h,m = input('(AM 12 00) 형식으로 시간을 입력하시오 :').split()

            h = int(h)
            m = int(m)

            while True: #am,pm을 소문자로 입력해도 인식할 수 있게 upper() 사용, 시간과 분의 범위 설정
                if day.upper() not in ['AM','PM'] or not (0<= h <=12) or not (0<= m <60):
                    print('잘못된 입력입니다. 다시 입력해주세요')
                    day,h,m = input('(AM/PM 12 00) 형식으로 시간을 입력하시오 :').split()
                else:
                    break
            break
        except:
            print('잘못된 입력입니다. 다시 입력해주세요')

    if day.upper() == 'PM': # 계산하기 쉽게 시간의 범위를 0~24로 하여 계산
        h += 12
    
    # 수면시간 계산한 값들을 변수에 넣어준다.
    i1,j1 = cal_time(h-9,m)
    i2,j2 = cal_time(h-7,m-30)
    i3,j3 = cal_time(h-6,m)
    i4,j4 = cal_time(h-4,m-30)

    #결과값을 출력한다
    print_time(cal_time(h-9,m)[0],cal_time(h-9,m)[1])
    print_time(cal_time(h-7,m-30)[0],cal_time(h-7,m-30)[1])
    print_time(cal_time(h-6,m)[0],cal_time(h-6,m)[1])
    print_time(cal_time(h-4,m-30)[0],cal_time(h-4,m-30)[1])

    # 그래프를 그릴 함수의 매개변수 만들기
    time_list = []
    time_list.append([i1,j1])
    time_list.append([i2,j2])
    time_list.append([i3,j3])
    time_list.append([i4,j4])

    # 그래프 그리는 함수 호출
    draw_graph(time_list,n)



elif n == '2':
    while True:
        try:
            day,h,m = input('(AM 12 00) 형식으로 시간을 입력하시오 :').split()

            h = int(h)
            m = int(m)

            while True:
                if day.upper() not in ['AM','PM'] or not (0<= h <=12) or not (0<= m <60):
                    print('잘못된 입력입니다. 다시 입력해주세요')
                    day,h,m = input('(AM/PM 12 00) 형식으로 시간을 입력하시오 :').split()
                else:
                    break
            break
        except:
            print('잘못된 입력입니다. 다시 입력해주세요')

    if day.upper() == 'PM':
        h += 12

    i1,j1 = cal_time(h+4,m+30)
    i2,j2 = cal_time(h+6,m)
    i3,j3 = cal_time(h+7,m+30)
    i4,j4 = cal_time(h+9,m)

    print_time(i1,j1)
    print_time(i2,j2)
    print_time(i3,j3)
    print_time(i4,j4)



    time_list = []
    time_list.append([i1,j1])
    time_list.append([i2,j2])
    time_list.append([i3,j3])
    time_list.append([i4,j4])

    draw_graph(time_list,n)


else:
    now = datetime.now()
    h = now.hour
    m = now.minute
    
    i1,j1 = cal_time(h+4,m+44)
    i2,j2 = cal_time(h+8,m+14)
    i3,j3 = cal_time(h+8,m+44)
    i4,j4 = cal_time(h+10,m+14)

    print_time(i1,j1)
    print_time(i2,j2)
    print_time(i3,j3)
    print_time(i4,j4)
    
    
    
    time_list = []
    time_list.append([i1,j1])
    time_list.append([i2,j2])
    time_list.append([i3,j3])
    time_list.append([i4,j4])

    draw_graph(time_list,n)




