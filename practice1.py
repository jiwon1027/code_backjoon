print("2128805-박수빈")

# x=[-10,10] 구간에서 총 4개의 그래프를 4분면에 나눠서 그리는 프로그램을 작성하시오. 1사분면에 y=2*x-3, 2사분면에 y=-2*x-3, 3사분면에 y=2*x+3, 4사분면에 y=-2*x+3의 그래프를 그리시오.

#time,x,y를 배열로 잡음.
time=[]
x=[]
y=[]
#파일로부터 데이터를 불러들임.
inputfile=open("C:\Temp\GPS_data.csv",encoding='UTF-8-sig')
line=inputfile.readline().rstrip()
#반복문 while을 사용하여 특정한 조건만을 만족하는 데이터를 뽑아냄.
while line!="":
      linedata=line.split(",")
      time.append(float(linedata[0]))
      x.append(float(linedata[1]))
      y.append(float(linedata[2]))
      line=inputfile.readline().rstrip()
#time,x,y배열에 저장하는 코드를 구함
print("time :",time)
print("x :",x)
print("y :",y)
inputfile.close()

# 선박이 이동하는 영역을 추정하기 위해 x의 최소값과 최대값, y의 최소값과 최대값을 출력하는 코드를 작성함
print('x의 최소/최대값:',min(x),'/',max(x))
print('y의 최소/최대값:',min(y),'/',max(y))

# 이동한 총 거리를 계산하여 출력하는 코드
result=0
for i in range(len(x)-1):
    d=(((x[i]-x[i+1])**2+(y[i]-y[i+1])**2)**0.5)
    result=result+d
print(result)

#선박의 평균속력을 계산하는 코드를 작성하라
print(result/(time[31]-time[0]))

# No.5
def getVelocity(time,x,y):
    vx = []
    vy = []
    for i in range(len(time)-1):
        vx.append(abs(x[i+1] - x[i]) / (time[i+1] - time[i]))
        vy.append(abs(y[i+1] - y[i]) / (time[i+1] - time[i]))
    #No.6
    return vx,vy
#No.7
speed = []
for i in range(len(x)-1):
    distance=(((x[i]-x[i+1])**2+(y[i]-y[i+1])**2)**0.5)
    speed.append(distance/(time[i+1] - time[i]))
print('선박의 최대 속력 = ',max(speed))
print('선박의 최대 속력 발생 시간 = ',time[speed.index(max(speed))])

#No.8
vx = []
vy = []
time.pop(0)

vx, vy = getVelocity(time,x,y)
import math
with open('GPS_analysis.dat', 'w') as file:
    file.write('시간 x위치 y위치 Vx Vy 진행방향(degree)' + '\n')
    for i in range(len(time)-1):
        theta = math.atan2(abs(y[i + 1] - y[i]), abs(x[i + 1] - x[i]))
        file.write(str(time[i]) +' '+ str(round(x[i],6)) \
                   +' '+str(round(y[i],6)) +' '+ str(round(vx[i],6)) +' '\
                   + str(round(vy[i],6)) + ' ' + str(round(math.degrees(theta),6)) + '\n')
