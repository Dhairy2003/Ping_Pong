from turtle import Turtle
SPEED = 12
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.x_moving = SPEED
        self.y_moving = SPEED
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.penup()

    def move(self):
        x = self.xcor()
        y = self.ycor()
        self.goto(x + self.x_moving, y + self.y_moving)

    def bounce(self):
        self.y_moving = -1 * self.y_moving

    def slider_bounce(self):
        self.x_moving = -1 * self.x_moving

    def reset(self):
        self.goto(0, 0)
        self.slider_bounce()

