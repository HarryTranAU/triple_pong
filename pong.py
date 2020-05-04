# Using the Pong tutorial by @TokyoEdTech
# Expanded to triple pong by myself(Harry)

import turtle
import os
import random

wn = turtle.Screen()
wn.title("Triple Pong")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# Score
score_a = 0
score_b = 0

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("red")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350,0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("blue")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350,0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0,0)
# Ball speed (change accordingly to computer speed)
ball.dx = 0.2
ball.dy = 0.2

# Ball 2
ball2 = turtle.Turtle()
ball2.speed(0)
ball2.shape("square")
ball2.color("white")
ball2.penup()
ball2.goto(0,0)
# Ball speed (change accordingly to computer speed)
ball2.dx = -0.2
ball2.dy = -0.2

# Ball 3
ball3 = turtle.Turtle()
ball3.speed(0)
ball3.shape("square")
ball3.color("orange")
ball3.penup()
ball3.goto(0,0)
# Ball speed (change accordingly to computer speed)
ball3.dx = 0.11
ball3.dy = 0.11

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Red: 0  Blue: 0", align="center", font=("Courier", 24, "normal"))

# Function
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)

# Keyboard binding
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")

# Main game loop
while True:
    wn.update()

    # Move the Ball
    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)

    ball2.setx(ball2.xcor()+ball2.dx)
    ball2.sety(ball2.ycor()+ball2.dy)

    ball3.setx(ball3.xcor()+ball3.dx)
    ball3.sety(ball3.ycor()+ball3.dy)

    # Border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        os.system("aplay bounce.wav&")

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        os.system("aplay bounce.wav&")

    if ball2.ycor() > 290:
        ball2.sety(290)
        ball2.dy *= -1
        os.system("aplay bounce.wav&")

    if ball2.ycor() < -290:
        ball2.sety(-290)
        ball2.dy *= -1
        os.system("aplay bounce.wav&")

    if ball3.ycor() > 290:
        ball3.sety(290)
        ball3.dy *= -1
        os.system("aplay bounce.wav&")

    if ball3.ycor() < -290:
        ball3.sety(-290)
        ball3.dy *= -1
        os.system("aplay bounce.wav&")

    if ball.xcor() > 390:
        ball.goto(0, random.randint(-290, 290))
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Red: {}  Blue: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

    if ball.xcor() < -390:
        ball.goto(0, random.randint(-290, 290))
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Red: {}  Blue: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

    if ball2.xcor() > 390:
        ball2.goto(0, random.randint(-290, 290))
        ball2.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Red: {}  Blue: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

    if ball2.xcor() < -390:
        ball2.goto(0, random.randint(-290, 290))
        ball2.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Red: {}  Blue: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

    if ball3.xcor() > 390:
        ball3.goto(0, random.randint(-290, 290))
        ball3.dx *= -1
        score_a += 2
        pen.clear()
        pen.write("Red: {}  Blue: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

    if ball3.xcor() < -390:
        ball3.goto(0, random.randint(-290, 290))
        ball3.dx *= -1
        score_b += 2
        pen.clear()
        pen.write("Red: {}  Blue: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

    # Paddle and ball collisions
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1
        os.system("aplay bounce.wav&")

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1
        os.system("aplay bounce.wav&")

    if (ball2.xcor() > 340 and ball2.xcor() < 350) and (ball2.ycor() < paddle_b.ycor() + 40 and ball2.ycor() > paddle_b.ycor() - 40):
        ball2.setx(340)
        ball2.dx *= -1
        os.system("aplay bounce.wav&")

    if (ball2.xcor() < -340 and ball2.xcor() > -350) and (ball2.ycor() < paddle_a.ycor() + 40 and ball2.ycor() > paddle_a.ycor() - 40):
        ball2.setx(-340)
        ball2.dx *= -1
        os.system("aplay bounce.wav&")

    if (ball3.xcor() > 340 and ball3.xcor() < 350) and (ball3.ycor() < paddle_b.ycor() + 40 and ball3.ycor() > paddle_b.ycor() - 40):
        ball3.setx(340)
        ball3.dx *= -1
        os.system("aplay bounce.wav&")

    if (ball3.xcor() < -340 and ball3.xcor() > -350) and (ball3.ycor() < paddle_a.ycor() + 40 and ball3.ycor() > paddle_a.ycor() - 40):
        ball3.setx(-340)
        ball3.dx *= -1
        os.system("aplay bounce.wav&")
