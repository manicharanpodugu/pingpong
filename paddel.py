from turtle import Turtle
class Paddel:
    def __init__(self,dir):
           self.x=dir*650
           self.peddel=Turtle('square')
           self.peddel.hideturtle()
           self.peddel.up()
           self.peddel.speed("fastest")
           self.peddel.color('white')
           self.peddel.shapesize(stretch_wid=1,stretch_len=5)
           self.peddel.goto(self.x,0)
           self.peddel.setheading(90)
           self.peddel.showturtle()
                   
    def moveup(self):
          self.peddel.fd(20) 
    def movedown(self):
           self.peddel.back(20)
                     