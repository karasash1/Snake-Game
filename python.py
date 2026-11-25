import turtle
import time
import random
delay = 0.15
score = 0
high_score = 0
# the screen
wn = turtle.Screen()
wn.title("Snake Game by karas")
wn.bgcolor("black")
wn.setup(width=1000, height=1000)
wn.tracer(0)

#pictures
wn.addshape("head.gif")
wn.addshape("seg.gif")


# snake head
head = turtle.Turtle()
head.speed(0)
head.color("green")
head.shape("head.gif")
head.shapesize(2,2)
head.penup()
head.goto(0, 0)
head.direction = "stop"

# snake food
food = turtle.Turtle()
food.speed(0)
food.color("red")
food.shape("circle")
food.shapesize(1.5,1.5)
food.penup()
food.goto(0, 100)
segs = []

# score
pen = turtle.Turtle()
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 430)
pen.write("Score: 0 High Score: 0", align="center", font=("Times New Roman", 24, "normal"))

#game over
G_over = turtle.Turtle()
G_over.color("yellow")
G_over.penup()
G_over.hideturtle()
G_over.speed(0)
G_over.goto(0,0)


#speed levels
level = turtle.Turtle()
level.speed(0)
level.color("white")
level.hideturtle()
level.penup()
level.goto(0, 400)
level.write("Speed: Medium", align="center", font=("Times New Roman", 16,"normal"))

#the Easy button
E_btn = turtle.Turtle()
E_btn.color("yellow")
E_btn.shape("square")
E_btn.penup()
E_btn.goto(-350, -450)
E_btn.speed(0)

#mediam button
M_btn = turtle.Turtle()
M_btn.speed(0)
M_btn.shape("square")
M_btn.penup()
M_btn.color("green")
M_btn.goto(0, -450)

#hard button
H_btn = turtle.Turtle()
H_btn.speed(0)
H_btn.color("red")
H_btn.shape("square")
H_btn.penup()
H_btn.goto(350, -450)

#label for each level
lable = turtle.Turtle()
lable.color("white")
lable.penup()
lable.hideturtle()
lable.speed(0)
lable.goto(-300, -460)
lable.write("Easy", align="center", font=("Times New Roman", 16, "normal"))

lable.goto(50, -460)
lable.write("Midium", align="center", font=("Times New Roman", 16, "normal"))

lable.goto(400, -460)
lable.write("Hard", align="center" , font=("Times New Roman", 16, "normal"))

#functions for buttons
def easy(x, y):
    global delay
    delay = 0.2
    level.clear()
    level.write("Speed: Easy", align="center", font=("Times New Roman", 16, "normal"))

def midium(x, y):
    global delay
    delay = 0.15
    level.clear()
    level.write("Speed: Midium", align="center", font=("Times New Roman", 16, "normal"))

def hard(x, y):
    global delay
    delay = 0.09
    level.clear()
    level.write("Speed: Hard", align="center", font=("Times New Roman", 16, "normal"))

E_btn.onclick(easy)
M_btn.onclick(midium)
H_btn.onclick(hard)
# functions (note: ! for the inverse move)


def go_up():
    if head.direction != "down":
        head.direction = "up"


def go_down():
    if head.direction != "up":
        head.direction = "down"


def go_right():
    if head.direction != "left":
        head.direction = "right"


def go_left():
    if head.direction != "right":
        head.direction = "left"


def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 45)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 45)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 45)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 45)


# keyboard keys
wn.listen()
wn.onkeypress(go_up, "w")
wn.onkeypress(go_up, "Up")
wn.onkeypress(go_down, "s")
wn.onkeypress(go_down, "Down")
wn.onkeypress(go_right, "d")
wn.onkeypress(go_right, "Right")
wn.onkeypress(go_left, "a")
wn.onkeypress(go_left, "Left")


# main game loop
while True:
    wn.update()
    # check for collisions
    x = head.xcor()
    y = head.ycor()
    hit_Rwall = x > 470
    hit_Lwall = x < -470
    hit_Twall = y > 450
    hit_Bwall = y < -450
    if hit_Rwall or hit_Lwall or hit_Twall or hit_Bwall:
        G_over.write("Game Over", align="center", font=("Times New Roman", 40, "bold"))
        wn.update()
        time.sleep(1)
        G_over.clear()
        head.goto(0, 0)
        head.direction = "stop"

        # hide segments
        for seg in segs:
            seg.goto(1000, 1000)
        segs.clear()
        # resting the score
        score = 0
        pen.clear()
        score_T = "Score: " + str(score) + " High Score: " + str(high_score) 
        pen.write(score_T, align="center", font=("Times New Roman", 24, "normal"))

    if head.distance(food) < 40:
        # move food to random places
        x = random.randint(-430, 430)
        y = random.randint(-430, 430)
        food.goto(x, y)

        # adding a segemnt
        new_seg = turtle.Turtle()
        new_seg.speed(0)
        new_seg.color("dark green")
        new_seg.shape("seg.gif")
        new_seg.shapesize(2, 2)
        new_seg.penup()
        segs.append(new_seg)
        # score increasing
        score = score + 10
        if score > high_score:
            high_score = score
        pen.clear()
        score_T = "Score: " + str(score) + " High Score: " + str(high_score) 
        pen.write(score_T, align="center", font=("Times New Roman", 24, "normal"))
        

# move the end segments first in reverse order

    T_segs = len(segs)
    for index in range(T_segs - 1, 0, -1):
        Fr_segs = segs[index - 1]
        Cur_segs = segs[index]

        x = Fr_segs.xcor()
        y = Fr_segs.ycor()
        Cur_segs.goto(x, y)
# move the segments behind the head
    if len(segs) > 0:
        x = head.xcor()
        y = head.ycor()
        segs[0].goto(x, y)

    move()
# head collision
    for seg in segs:
        if seg.distance(head) < 40:
            G_over.write("Game Over", align="center", font=("Times New Roman", 40, "bold"))
            wn.update()
            head.goto(0, 0)
            time.sleep(1)
            G_over.clear()
            head.direction = "stop"
            print("Game Over")
            for seg in segs:
                seg.goto(1000, 1000)
            segs.clear()
            score = 0
            pen.clear()
            score_T = "Score: " + str(score) + " High Score: " + str(high_score) 
            pen.write(score_T, align="center", font=("Times New Roman", 24, "normal"))

    time.sleep(delay)
