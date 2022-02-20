from turtle import Turtle

class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('square')
        self.shapesize(stretch_wid=5, stretch_len=1) # (square original size(20X20) need to stretch to (100X20)
        self.color('white')
        self.goto(position)
        
        
    def go_up(self):
        new_y = self.ycor() + 40
        self.goto(self.xcor(), new_y)
        
    def go_down(self):
        new_y = self.ycor() - 40
        self.goto(self.xcor(), new_y)
        
        
