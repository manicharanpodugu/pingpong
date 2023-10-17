from turtle import Screen, Turtle
from paddel import Paddel
from score import Score
from pong import Pong
screen = Screen()
screen.tracer(0)
screen.bgcolor("black")
screen.setup(1400, 1000)
seprator = Turtle("square")
seprator.pencolor('white')
seprator.hideturtle()
seprator.pensize(10)
seprator.up()
seprator.speed("fastest")
seprator.goto(0, -380)
seprator.setheading(90)
for _ in range(19):
    seprator.pendown()
    seprator.fd(20)
    seprator.up()
    seprator.fd(20)

player_1 = Paddel(-1)
player_2 = Paddel(1)
p1_score = Score(-1)
p2_score = Score(1)
pong = Pong()
game_status = True
level=1

def end():
    global game_status
    game_status = False


while game_status:
    screen.update()
    screen.listen()
    screen.onkey(key="Up", fun=player_2.moveup)
    screen.onkey(key="Down", fun=player_2.movedown)
    screen.onkey(key="w", fun=player_1.moveup)
    screen.onkey(key="s", fun=player_1.movedown)
    screen.onkey(key="l", fun=end)
    pong.move()
    if (pong.xcor() < 650 and pong.xcor() > -650) and (pong.ycor() > 380 or pong.ycor() < -380):
        pong.bounce()
        level+=1
    elif -20 < player_1.peddel.xcor()-pong.xcor() < 0 and -50 < player_1.peddel.ycor()-pong.ycor() < 50:
        pong.x_move *= -1
        level+=1
    elif 0 < player_2.peddel.xcor()-pong.xcor() < 20 and -50 < player_2.peddel.ycor()-pong.ycor() < 50:
        pong.x_move *= -1
        level+=1
    elif (pong.xcor() < -650):
        p1_score.inc_score()
        if pong.x_move > 0:
            pong.x_move *= -1
            level+=1
        pong.goto(0, 0)
    elif (pong.xcor() > 650):
        p2_score.inc_score()
        if pong.x_move < 0:
            pong.x_move *= -1
            level+=1
        pong.goto(0, 0)
    if level%20==0:
        pong.level+=1

screen.exitonclick()
