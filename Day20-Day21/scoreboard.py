from turtle import Turtle

ALIGN = 'center'
FONT = ('Courier', 24, 'normal')


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.goto(0, 260)
        self.color('white')
        self.hideturtle()
        self.update_score()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game Over !!", align=ALIGN, font=FONT)

    def update_score(self):
        self.write(f"Score : {self.score}", align=ALIGN, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()
