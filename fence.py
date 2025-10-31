from turtle import Turtle

class Fence(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-265, -190)
        self.pendown()
        self.pensize(3)
        self.line()
        
    def line(self):
        for _ in range(2):
            self.left(90)
            self.forward(410)
            self.right(90)
            self.forward(535)
            self.right(180)


