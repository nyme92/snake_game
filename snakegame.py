# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    snakegame.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: muelfaha <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/05/13 04:14:23 by muelfaha          #+#    #+#              #
#    Updated: 2019/05/13 04:53:22 by muelfaha         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import turtle
import time
import random

delay = .1

# Compare and Keep Score
score = 0
score_board = 0

# Create Screen
sn = turtle.Screen()
sn.title("The Original snake Game By Muhammad Elfaham")
sn.bgcolor("black")
sn.setup(width=600, height=600)
sn.tracer(0)

# Create Head of snake
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("blue")
head.penup()
head.goto(0,0)
head.direction = "stop"

# Food
food = turtle.Turtle()
food.speed(0)
food.shape("square")
food.color("red")
food.penup()
food.goto(0,100)

# Array to add to snakelength everytime food is eaten
snakes = []

# Pen to write Score
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.color("white")
pen.write("Score: 0 Good Luck!", align="center", font=("Comic Sans", 40, "bold"))

# Functions for Movements

def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_dosn():
    if head.direction != "up":
        head.direction = "down"

def go_right():
    if head.direction != "left":
        head.direction = "right"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def move():
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)
        
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

def exit ():
    turtle.bye()

sn.listen()
sn.onkey(go_up, "Up")
sn.onkey(go_dosn, "Down")
sn.onkey(go_left, "Left")
sn.onkey(go_right, "Right")
sn.onkey(exit, "q")

# Main Game
while True:
    sn.update()
    
    for snake in snakes:
        if snake.distance(head) < 20:
           print("Game Over: Your Score is: {} ".format(score,score_board))
           quit()
           
# If snake collides with border, snake appears on other side 
    if head.xcor() > 290:
        head.setx(-290)
    if head.xcor() < -290:
        head.setx(290)
    if head.ycor() > 290:
        head.sety(-290) 
    if head.ycor() < -290:
        head.sety(290)
# IF snake collides with food, move food to another place and add to snake 
    if head.distance(food) < 20:
        x = random.randint(-290,290)
        y = random.randint(-290, 290)
        food.goto(x, y)
        new_snake = turtle.Turtle()
        new_snake.speed(0)
        new_snake.shape("square")
        new_snake.color("blue")
        new_snake.penup()
        snakes.append(new_snake)

# Increase the speed of the snake by shortening the delay
        delay -= 0.001
# Increase Score
        score += 8
    if score > score_board:
        score_board = score
        pen.clear()
        pen.write("Score: {}  ".format(score,score_board), align="center", font=("Comic Sans", 40, "bold"))


#Move the end snakes first in reverse order to move properly onscreen

    for i in range(len(snakes)-1,0,-1):
        x = snakes[i -1].xcor()
        y = snakes[i - 1].ycor()
        snakes[i].goto(x, y)

#Move snakes 0 to where the head is
    if len(snakes) > 0:
       x = head.xcor()
       y = head.ycor()
       snakes[0].goto(x,y)

    move()
    time.sleep(delay)

sn.mainloop()
