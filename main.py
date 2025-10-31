import time
from turtle import Turtle, Screen
from fence import Fence
from scoreboard import ScoreBoard
from snake import Snake
from food import Food

# PLAY-GROUND
screen = Screen()
screen.screensize(600, 600)
screen.bgpic("snake_bgp.png")
screen.tracer(0)

# FENCE
fence = Fence()

# SCORE-BOARD
score = ScoreBoard()

# SNAKE
mike = Snake()

# FOOD
food = Food()

# KEY CONTROLS
screen.listen()
screen.onkey(mike.up, "Up")
screen.onkey(mike.down, "Down")
screen.onkey(mike.left, "Left")
screen.onkey(mike.right, "Right")

game_is_on = True 
while game_is_on:
    screen.update()
    time.sleep(0.1)
    mike.move_forward()
    
    # DETECT COLLISION WITH FOOD
    if mike.head.distance(food) < 15:
        food.refresh()
        mike.extend()
        score.increase_score()
        
    # DETECT COLLISION WITH WALL
    if mike.head.xcor() > 265 or mike.head.xcor() < -265 or mike.head.ycor() > 200 or mike.head.ycor() < -199:
        score.game_over()
        game_is_on = False

screen.exitonclick()