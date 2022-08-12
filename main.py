import time
from turtle import Screen
from player import Player
from cars import Cars
from level import Level


screen = Screen()
screen.title('Turtle Crossing')
screen.setup(width=600,height=600)
screen.tracer(0)
screen.colormode(255)

player = Player()
car = Cars()
level = Level()

screen.listen()
screen.onkeypress(key='w',fun=player._up)

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.create_cars()
    car.car_move()
    for item in car.cars:
        if item.distance(player) < 20:
            level.game_over()
            game_is_on = False
    if player.ycor() > 290:
        player.goto(0,-280)
        level.new_level()
        car.increase_speed()


screen.exitonclick()