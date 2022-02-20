from turtle import Turtle
FONT = ('Courier', 80, 'normal')

class Scoreboard(Turtle):
    super().__init__()
    self.l_score = 0
    self.r_score = 0
    self.color('black')
    self.penup()
    self.hideturtle()
    self.update_scoreboard()
    
    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align='center', font=FONT)
        self.goto(100, 200)
        self.write(self.r_score, align='center', font=FONT)
    
    def l_point(self):
        self.score += 1
        self.update_scoreboard()
    
    ded r_point(self):
        self.score += 1
        self.update_scoreboard()
        
