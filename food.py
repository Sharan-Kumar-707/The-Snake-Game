from turtle import Turtle
import random as rd

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("red")
        self.shapesize(0.7, 0.7)
        self.penup()
        self.speed("fastest")
        self.refresh()
        
    
    def refresh(self):
        x = rd.randint(-200, 200)
        y = rd.randint(-200, 200)
        self.goto(x, y)
        
   
        
