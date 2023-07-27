from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 10, "bold")


class Score(Turtle):
    def __init__(self):
        super().__init__()
        # arg, move=False, align='left', font=('Arial', 8, 'normal')
        self.score = 0
        with open("data.txt") as file:
            self.high_score = int(file.read())
        # self.new_value_score = self.new_value()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 280)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}  High score: {self.high_score}", move=False, align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        with open("data.txt", mode="w") as file:
            file.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", move=False, align=ALIGNMENT, font=FONT)

    def upgrade_score(self):
        self.score += 1
        self.update_scoreboard()



