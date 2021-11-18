import turtle
import time
import random
def draw(value):
    if value == 0: #RYAN
        turtle.forward(100)
        turtle.left(90)
        turtle.forward(100)
        turtle.left(90)

    if value == 1: #MUZI
        turtle.forward(200)
        turtle.left(90)
        turtle.forward(200)
        turtle.left(90)

    if value == 2: #APEACH
        turtle.forward(200)
        turtle.left(90)
        turtle.forward(200)
        turtle.left(90)

    if value == 3: #JAY-G
        turtle.forward(50)
        turtle.left(90)
        turtle.forward(50)
        turtle.left(90)

    if value == 4: #FRODO
        turtle.forward(100)
        turtle.right(90)
        turtle.forward(100)
        turtle.left(90)

    if value == 5: #NEO
        turtle.forward(100)
        turtle.right(90)
        turtle.forward(100)
        turtle.right(90)

    if value == 6: #TUBE
        turtle.forward(100)
        turtle.right(90)
        turtle.forward(100)
        turtle.right(90)

    if value == 7: #CON
        turtle.forward(100)
        turtle.right(90)
        turtle.forward(100)
        turtle.right(90)

kakao_friends = ['RYAN','MUZI','APEACH','JAY-G','FRODO','NEO','TUBE','CON']
cnt = 0
scr = turtle.Screen()

scr.setup(600, 377)

scr.bgpic("bg_main.gif")
scr.update()
time.sleep(2)

scr.bgpic("bg_select.gif")
scr.update()
time.sleep(2)

scr.setup(500, 800)
scr.bgpic('bg_game.gif')
scr.update()


while True:
    turtle.reset()
    turtle.speed(1)

    value = random.randrange(0,8)
    draw(value)

    answer = turtle.textinput("KaKao Friends","무엇일까요?(종료 : end 입력)")
    answer = answer.upper()

    if answer in kakao_friends:
        if kakao_friends[value] == answer:
            turtle.write('정답입니다!',False,"center",("굴림",20))
            cnt += 1
        else:
            turtle.write('틀렸습니다ㅠ',False,"center",("굴림",20))
    elif answer == 'end':
        turtle.reset()
        break
    else:
        turtle.write('카카오 친구들을 입력해주세요!', False, "center", ("굴림", 20))

    time.sleep(2)

turtle.penup()
turtle.goto(-50,100)
turtle.write('점수는 : ', False, "center", ("굴림", 20))
turtle.goto(50,100)
turtle.write(cnt, False, "center", ("굴림", 20))

turtle.exitonclick()


