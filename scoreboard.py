from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.setpos(0, 250)
        self.color('white')
        self.scor = 0
        with open('highscore.txt', mode='r') as fisier:
            scor_maxim = fisier.read()
            self.highscore = int(scor_maxim)
        self.actualizare_scor()
        self.hideturtle()

    def actualizare_scor(self):
        self.clear()
        self.write(f'Score = {self.scor} High score = {self.highscore}', move=False, align='center', font=('Arial', 12, 'normal'))


    def reset(self):
        if self.scor > self.highscore:
            self.highscore = self.scor
            scor_maxim = self.highscore
            scor_maxim = str(scor_maxim)
            with open('highscore.txt', mode='w') as fisier:
                fisier.write(scor_maxim)
        self.scor = 0
        self.actualizare_scor()

    # def joc_terminat(self):
    #     self.setpos(0, 0)
    #     self.write(f'GAME OVER', move=False, align='center', font=('Arial', 12, 'normal'))

    def marire_scor(self):
        self.scor += 1
        self.actualizare_scor()