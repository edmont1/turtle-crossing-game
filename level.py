from turtle import Turtle

class Level(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-270,250)
        self.value = 1
        self.level()

    def level(self):
        self.write(arg=f'Level: {self.value}', font=('courier', 20, 'bold'))

    def new_level(self):
        self.value += 1
        self.clear()
        self.level()

    def game_over(self):
        self.goto(0,0)
        self.write(arg=f'GAME OVER',align='center', font=('courier', 20, 'bold'))
