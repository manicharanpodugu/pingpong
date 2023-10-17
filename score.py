from turtle import Turtle
class Score(Turtle):
    def __init__(self,player):
        super().__init__()
        self.score=0
        self.color("white")
        self.up()
        self.hideturtle()
        self.goto(0,380)
        if player<0:
            self.dir="left"
        else :
           self.dir= "right"
        self.update() 
    def update(self):
        self.clear() 
        self.write(f"         SCORE IS :{self.score}         ",align=self.dir,font=("Verdana",40, 'normal'))
    def inc_score(self):
        self.score+=1
        self.update()    