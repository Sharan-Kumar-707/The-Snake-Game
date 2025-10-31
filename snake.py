from turtle import Turtle, Screen
POSITIONS = [(0,0), (-20,0), (-40,0)]
FORWARD_DIST = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    
    def __init__(self):
        self.segments = []
        self.create_segment()
        self.head = self.segments[0]
        
    def create_segment(self):
        for pos in POSITIONS:
            self.add_segment(pos)
            
    def add_segment(self, pos):
        self.new_segment = Turtle("circle")
        self.new_segment.color("blue")
        self.new_segment.penup()
        self.new_segment.goto(pos)
        self.segments.append(self.new_segment)
        
    def move_forward(self):
        for i in range(len(self.segments) - 1, 0, -1):
            x = self.segments[i -1].xcor()
            y = self.segments[i - 1].ycor()
            self.segments[i].goto(x, y)
        self.segments[0].forward(20)
    
    def extend(self):
        self.add_segment(self.segments[-1].position())
        
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
    
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)