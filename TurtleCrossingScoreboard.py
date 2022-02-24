from turtle import Turtle
FONT = ('courier', 24, 'normal')

class Scoreboard(Turtle):
  def __init__(self):
    super().__init__():
      self.level = 1
      self.color('black')
      self.penup()
      self.goto(-300, 260)
      self.update_scoreboard()
      self.hideturtle()
      
  def update_scoreboard(self):
    self.write(f'Level: {self.level}', align='left', font=FONT)
  
  def game_over(self):
    self.write('GAME OVER', align='center', font=FONT)
    
  def increase_level(self):
    self.level += 1
    self.clear()
    self.update_scoreboard()
