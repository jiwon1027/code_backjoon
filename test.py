import random
import turtle

myTurtle, tX, tY, tSize = [None] * 4
playerTurtles = []
swidth, sheight = 500, 500

if __name__ == "__main__":
    turtle.title('거북 리스트 활용(정렬)')
    turtle.setup(width=swidth + 50, height=sheight + 50)
    turtle.screensize(swidth, sheight)


    for i in range(5):
        myTurtle = turtle.Turtle('turtle')
        tX = random.randrange(-swidth / 2, swidth / 2)
        tY = random.randrange(-sheight / 2, sheight / 2)
        r = random.random()
        g = random.random()
        b = random.random()
        #사이즈 설정
        tSize = random.randrange(1, 100)/10
        playerTurtles.append([myTurtle, tX, tY, tSize, r, g, b])
    #크기에 대한 오름차순 정렬
    sorted_Turtles = sorted(playerTurtles, key=lambda turtles: turtles[3])

    for index, tList in enumerate(sorted_Turtles[0:]):
        myTurtle = tList[0]
        myTurtle.color((tList[4], tList[5], tList[6]))
        myTurtle.pencolor((tList[4], tList[5], tList[6]))
        myTurtle.turtlesize(tList[3])
        myTurtle.penup()
        #각도 설정
        myTurtle.right(random.randrange(0, 360))

        if index == 0:
            myTurtle.goto(tList[1], tList[2])
            continue
        myTurtle.goto(sorted_Turtles[index - 1][1], sorted_Turtles[index - 1][2])

        myTurtle.pendown()
        myTurtle.goto(tList[1], tList[2])

turtle.done()
