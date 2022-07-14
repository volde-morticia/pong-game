from turtle import Turtle

class Scores(Turtle):

  def __init__(self):
    super().__init__()
    self.color("white")
    self.penup()
    self.hideturtle()
    self.score_1 = 0
    self.score_2 = 0
    self.update()

  def update(self):
    self.clear()
    self.goto(100, 200)
    self.write(self.score_1, align="center", font=("Courier", 40, "normal"))
    self.goto(-100, 200)
    self.write(self.score_2, align="center", font=("Courier", 40, "normal"))

  def point_1(self):
    self.score_1 += 1
    self.update()

  def point_2(self):
    self.score_2 += 1
    self.update()

  def game_over(self):
    pass