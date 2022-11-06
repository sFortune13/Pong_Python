import tkinter
import turtle
import os
import time

# Globals
paused = False

# Window config
wn = turtle.getscreen()
wn.title("The First Game- Pong")
wn.bgcolor("black")
wn.setup(width=800,height=600)
wn.tracer(0)

score_1 = 0
score_2 = 0

# Paddle Player 1

paddle_1 = turtle.Turtle()
paddle_1.speed(0)
paddle_1.shape("square")
paddle_1.color("white")
paddle_1.shapesize(stretch_wid=5, stretch_len=1)
paddle_1.penup()
paddle_1.goto(-350,0)

# Paddle Player 2

paddle_2 = turtle.Turtle()
paddle_2.speed(0)
paddle_2.shape("square")
paddle_2.color("white")
paddle_2.shapesize(stretch_wid=5, stretch_len=1)
paddle_2.penup()
paddle_2.goto(350,0)

# Ball

ball = turtle.Turtle()
ball_speed = 10
ball.speed(ball_speed)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx = 2
ball.dy = 2

# Pen

pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal"))

# Function

def paddle_1_up():
    y = paddle_1.ycor()
    y += 20
    paddle_1.sety(y)

def paddle_1_down():
    y = paddle_1.ycor()
    y -= 20
    paddle_1.sety(y)

def paddle_2_up():
    y = paddle_2.ycor()
    y += 20
    paddle_2.sety(y)

def paddle_2_down():
    y = paddle_2.ycor()
    y -= 20
    paddle_2.sety(y)

# def pause_game():
#     global paused
#     paused = True
#     wn.delay(100)

# Control bindings

wn.listen()
wn.onkeypress(paddle_1_up, "w")
wn.onkeypress(paddle_1_down, "s")
wn.onkeypress(paddle_2_up, "Up")
wn.onkeypress(paddle_2_down, "Down")

# Main game loop

while True:
    wn.update()

    time.sleep(.01)
    

    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking

    # Top and bottom
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
    
    elif ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    # Left and right
    if ball.xcor() > 350:
        score_1 += 1
        pen.clear()
        pen.write("Player 1: {}  Player 2: {}".format(score_1, score_2), align="center", font=("Courier", 24, "normal"))
        ball.goto(0, 0)
        ball.dx *= -1

    elif ball.xcor() < -350:
        score_2 += 1
        pen.clear()
        pen.write("Player 1: {}  Player 2: {}".format(score_1, score_2), align="center", font=("Courier", 24, "normal"))
        ball.goto(0, 0)
        ball.dx *= -1

    # Paddle and ball collisions
    if ball.xcor() < -340 and ball.ycor() < paddle_1.ycor() + 50 and ball.ycor() > paddle_1.ycor() - 50:
        ball.dx *= -1 
        ball_speed -= 1
        ball.speed(ball_speed)
        print(ball_speed)
    
    elif ball.xcor() > 340 and ball.ycor() < paddle_2.ycor() + 50 and ball.ycor() > paddle_2.ycor() - 50:
        ball.dx *= -1
        ball_speed -= 1
        ball.speed(ball_speed)
        print(ball_speed)
