from turtle import Turtle
import time
class Pong (Turtle):
   def  __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.level=1
        self.speed(10)
        self.up()
        self.x_move=10
        self.y_move=10
        
   def move(self):
       time.sleep(.1-0.001*self.level)
       self.goto(self.xcor()+self.x_move,self.ycor()+self.y_move)
   def bounce(self):
       self.y_move*=-1    
       