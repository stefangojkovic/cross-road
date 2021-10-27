from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.cars = []
        self.move_distance = STARTING_MOVE_DISTANCE
        self.num_cars = 5

    def add_car(self):
        random_choice = random.randint(1, self.num_cars)
        if random_choice == 1:
            car = Turtle()
            car.shape('square')
            car.shapesize(stretch_len=2, stretch_wid=1)
            car.color(random.choice(COLORS))
            car.penup()
            car.goto(280, random.randint(-250, 250))
            self.cars.append(car)

    def move_car(self):
        for car in self.cars:
            car.backward(self.move_distance)

    def level_up(self):
        self.move_distance += MOVE_INCREMENT
        if self.num_cars > 1:
            self.num_cars -= 1
