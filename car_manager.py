import random
from turtle import Turtle

CARS_COLOR = ["red", "blue", "orange", "purple", "green", "indigo"]
MOVE_BACKWARD = 5

class CarManager:
    def __init__(self):
        self.all_cars = []
        self.car_speed = MOVE_BACKWARD

    def create_cars(self):
        rand_car = random.randint(1, 6)
        if rand_car == 1:
            new_car = Turtle('square')
            new_car.shapesize(stretch_len=2, stretch_wid=1)
            new_car.color(random.choice(CARS_COLOR))
            new_car.penup()
            random_y = random.randint(-250, 250)
            new_car.goto(300, random_y)
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.car_speed)

    def level_up(self):
        self.car_speed += MOVE_BACKWARD
        
