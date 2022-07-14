from turtle import Screen
from paddle import Paddle
from ball import Ball
from scores import Scores
import time

s = Screen()
s.setup(800, 600)
s.bgcolor("black")
s.title("Pong Game")
s.tracer(0)
s.listen()

paddle_1 = Paddle((350, 0))
paddle_2 = Paddle((-350, 0))
ball = Ball()
scores = Scores()

s.onkey(paddle_1.go_up, "Up")
s.onkey(paddle_1.go_down, "Down")
s.onkey(paddle_2.go_up, "w")
s.onkey(paddle_2.go_down, "s")

print('''
W - moves the left paddle upwards
S - moves the left paddle downwards
UP - moves the right paddle upwards
DOWN - moves the right paddle downwards 
''')

sleep_time = 0.1
game_is_on = True
while game_is_on:
  time.sleep(sleep_time)
  s.update()
  ball.move()

  if ball.ycor() > 290 or ball.ycor() < -290:
    ball.bounce_y()

  if ball.distance(paddle_1) < 40 and ball.xcor() > 330:
    ball.bounce_x()
    sleep_time -= 0.01

  if ball.distance(paddle_2) < 40 and ball.xcor() > -330:
    ball.bounce_x()
    sleep_time -= 0.01

  if ball.xcor() > 390:
    ball.reset_position()
    sleep_time = 0.1
    scores.point_2()

  if ball.xcor() < -390:
    ball.reset_position()
    sleep_time = 0.1
    scores.point_1()