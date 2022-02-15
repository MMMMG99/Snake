from turtle import Turtle

COORDONATE = [(0, 0), (-20, 0), (-40, 0)]
DISTANTA_DE_MISCARE = 20
UP, DOWN, LEFT, RIGHT = 90, 270, 180, 0


class Sandu:
    def __init__(self):
        self.bucati_de_sandu = []
        self.creare_sandu()
        self.head = self.bucati_de_sandu[0]

    def creare_sandu(self):
        for ceva in COORDONATE:
            self.adauga_sandu(ceva)

    def adauga_sandu(self, pozitie):
        sandu = Turtle()
        sandu.color('white')
        sandu.shape('square')
        sandu.penup()
        sandu.goto(pozitie)
        self.bucati_de_sandu.append(sandu)

    def extindem_sandul(self):
        self.adauga_sandu(self.bucati_de_sandu[-1].position())

    def misca_sandu(self):
        for segment in range(len(self.bucati_de_sandu) - 1, 0, -1):
            # mergem de la coada la cap si luam coordonatele fiecarei bucati
            nou_x = self.bucati_de_sandu[segment - 1].xcor()
            nou_y = self.bucati_de_sandu[segment - 1].ycor()
            self.bucati_de_sandu[segment].goto(nou_x, nou_y)

        self.bucati_de_sandu[0].forward(DISTANTA_DE_MISCARE)

    def resetam_sandu(self):
        for seg in self.bucati_de_sandu:
            seg.goto(2000,2000)
        self.bucati_de_sandu.clear()
        self.creare_sandu()
        self.head = self.bucati_de_sandu[0]

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)