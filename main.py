from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import time

scn = Screen()
player = Player()
carmanager = CarManager()
score = Scoreboard()

scn.bgcolor('white')
scn.setup(width=600, height=600)
scn.tracer(0)

scn.listen()
scn.onkey(player.move_up, "Up")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    scn.update()
    carmanager.create_cars()
    carmanager.move_cars()

    for car in carmanager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            score.game_over()
    
    if player.is_at_finish_line():
        player.go_to_start()
        carmanager.level_up()
        score.increase_level()
    

scn.exitonclick()