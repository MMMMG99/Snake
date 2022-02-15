from turtle import Screen
from snake import Sandu
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title('Hai la joaca cu sarpele')
screen.tracer(0)

sarpe = Sandu()
food = Food()
scor = Scoreboard()

screen.listen()
screen.onkey(sarpe.up, 'Up')
screen.onkey(sarpe.down, 'Down ')
screen.onkey(sarpe.left, 'Left')
screen.onkey(sarpe.right, 'Right')

joaca = True
while joaca:
    screen.update()
    time.sleep(0.1)
    sarpe.misca_sandu()

    #gasim mancare
    if sarpe.head.distance(food) < 15:
        food.refresh()
        sarpe.extindem_sandul()
        scor.marire_scor()

    #gasim perete
    if sarpe.head.xcor() > 280 or sarpe.head.xcor() < -280 or sarpe.head.ycor() > 280 or sarpe.head.ycor() < -280:
        scor.reset()
        sarpe.resetam_sandu()

    #gasim corp
    for parte in sarpe.bucati_de_sandu[1:]:
        if sarpe.head.distance(parte) < 10:
            scor.reset()
            sarpe.resetam_sandu()


screen.exitonclick()