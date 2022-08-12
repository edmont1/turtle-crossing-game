from turtle import Turtle

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.setheading(90)
        self.penup()
        self.goto(0,-280)

    def _up(self):
        self.goto(0,self.ycor() + 10)




