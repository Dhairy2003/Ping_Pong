from turtle import Turtle
SPEED = 25

class Slider(Turtle):
    def __init__(self, cords):
        super().__init__()
        self.shape("square")
        self.move_speed = SPEED
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color("white")
        self.goto(cords)

    def moveup(self):
        if self.ycor() < 280:
            cur_x = self.xcor()
            cur_y = self.ycor()
            self.goto(cur_x, cur_y + self.move_speed)

    def movedown(self):
        if self.ycor() > -280:
            cur_x = self.xcor()
            cur_y = self.ycor()
            self.goto(cur_x, cur_y - self.move_speed)

