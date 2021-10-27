from turtle import Turtle
FONT = ("Courier", 24, "normal")
ALIGNMENT = 'center'


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.color("black")
        self.penup()
        self.goto(-260, 260)
        self.update_scoreboard()
        self.hideturtle()

    def increase_score(self):
        self.level += 1
        self.clear()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Level: {self.level}", font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("Game over", font=FONT, align=ALIGNMENT)
