import time
from turtle import Turtle, Screen
from slider import Slider
from ball import Ball


COORDS = [(-350, 0), (350, 0)]

screen = Screen()
screen.bgcolor("black")
screen.listen()
screen.title("Ping Pong")
screen.setup(width=800, height=600)
screen.tracer(0)

r_slider = Slider(COORDS[1])
l_slider = Slider(COORDS[0])
ball = Ball()

screen.onkey(key="w", fun=l_slider.moveup)
screen.onkey(key="s", fun=l_slider.movedown)
screen.onkey(key="Up", fun=r_slider.moveup)
screen.onkey(key="Down", fun=r_slider.movedown)

playing = True
while playing:
    screen.update()
    time.sleep(0.06)
    ball.move()
    if ball.ycor() >= 280 or ball.ycor() <= -280:
        ball.bounce()
    if ball.distance(r_slider) < 50 and ball.xcor() > 330 or ball.distance(l_slider) < 50 and ball.xcor() < -330:
        ball.slider_bounce()
    if ball.xcor() > 380 or ball.xcor() < -380:
        ball.reset()





screen.exitonclick()