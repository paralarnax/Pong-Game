# import turtle module
import turtle

# Setup
wn = turtle.Screen()
wn.tracer(120)
wn.title("Pong by @Paralarnax")
wn.bgcolor("white")
wn.setup(width=800, height=600)
wn.tracer(0)

# Score 
score_a = 0
score_b = 0

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0) 
paddle_a.shape("square")
paddle_a.color("black")
paddle_a.shapesize(stretch_len=1, stretch_wid=5)
paddle_a.penup()
paddle_a.goto(-350, 0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("black")
paddle_b.shapesize(stretch_len=1, stretch_wid=5)
paddle_b.penup()
paddle_b.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("black")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.3
ball.dy = 0.3

# Score
score = turtle.Turtle()
score.speed(0)
score.color("black")
score.penup()
score.hideturtle()
score.goto(0, 250)
score.write("Player A: 0    Player B: 0", align="center", font=("JetBrains Mono", 16, "normal"))

# Paddle A up
def paddle_a_up():
    y = paddle_a.ycor()
    y += 10
    paddle_a.sety(y)

# Paddle A down
def paddle_a_down():
    y = paddle_a.ycor()
    y -= 10
    paddle_a.sety(y)

# Paddle B up
def paddle_b_up():
    y = paddle_b.ycor()
    y += 10
    paddle_b.sety(y)

# Paddle B down
def paddle_b_down():
    y = paddle_b.ycor()
    y -= 10 
    paddle_b.sety(y)

# Movement 
wn.listen()
wn.onkeypress(paddle_a_up, 'w')
wn.onkeypress(paddle_a_down, 's')
wn.onkeypress(paddle_b_up, 'Up')
wn.onkeypress(paddle_b_down, 'Down')

# Main game loop
while True:
    wn.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx) 
    ball.sety(ball.ycor() + ball.dy) 

    # Border collision checking
    if ball.ycor() > 300:
        ball.sety(300)
        ball.dy *= -1

    if ball.ycor() < -300:
        ball.sety(-300)
        ball.dy *= -1

    if ball.xcor() > 400:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        score.clear()
        score.write("Player A: {}    Player B: {}".format(score_a, score_b), align="center", font=("JetBrains Mono", 16, "normal"))

    if ball.xcor() < -400:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        score.clear()
        score.write("Player A: {}    Player B: {}".format(score_a, score_b), align="center", font=("JetBrains Mono", 16, "normal"))

    # Paddle collision Checking
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() > paddle_b.ycor() - 50 and ball.ycor() < paddle_b.ycor() + 50):
        ball.setx(340)
        ball.dx *= -1
    
    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() > paddle_a.ycor() - 50 and ball.ycor() < paddle_a.ycor() + 50):
        ball.setx(-340)
        ball.dx *= -1