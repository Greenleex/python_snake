from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0,260)
        self.score = 0
    def write_score(self):
        self.clear()
        self.write(f'Score: {self.score}', False, align="center", font=("Arial", 20, "normal"))
    def update_score(self):
        self.score += 1

    def game_over(self):
        self.goto(0,0)
        self.write(f'GAME OVER', False, align="center", font=("Arial", 20, "normal"))