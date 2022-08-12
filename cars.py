from turtle import Turtle
import random



class Cars:
    def __init__(self):
        self.speed = 6
        self.cars = []


    def create_cars(self):
        while len(self.cars) < random.randint(1,20):
            car = Turtle('square')
            car.penup()
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.setpos(random.randint(300,600), random.randint(-250, 250))
            car.color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            self.cars.append(car)

    def car_move(self):
        for index,car in enumerate(self.cars):
            car.setx(car.xcor() - self.speed)
            if car.xcor() < -340:
                self.cars.pop(index)
                car.ht()


    def increase_speed(self):
        self.speed += 2




