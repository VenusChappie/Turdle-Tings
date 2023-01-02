import turtle
import random
import Turdle_Tings
import colorsys

turtle.shape("turtle")
turtle.left(90)
turtle.bgcolor("black")
turtle.color("yellow", "orange")
turtle.title("turtle Tings Doing The Tings")
turtle.pensize(5)
turtle.pencolor("yellow")
screen = turtle.Screen()
screen.setup(500,500, startx = 50,
         starty = -200)
turtle.goto(0,0)

def star_spiral():
    turtle.clear()
    turtle.speed(70)
    turtle.pensize(4)
    n = 30   
    x = 144   
    angle = 30 
    
    for i in range(n):
        
        turtle.pendown()
        turtle.colormode(255)
          
        a = random.randint(0, 255)
        b = random.randint(0, 255)
        c = random.randint(0, 255)
          
        # setting the outline 
        # and fill colour
        turtle.pencolor(a, b, c)
        turtle.fillcolor(a, b, c)
            
            # begins filling the star
        turtle.begin_fill()
          
        # loop for drawing each star
        for j in range(5):
                
            turtle.forward(5 * n-5 * i)
            turtle.right(x)
            turtle.forward(5 * n-5 * i)
            turtle.right(72 - x)
                
            # colour filling complete
            turtle.end_fill()
            
            # rotating for
            # the next star
            turtle.rt(angle)
    turtle.penup()
    turtle.home()
    

def square():
    turtle.clear()
    turtle.speed(50)

    angle = 3
    n = 5

    while n <= 200:
        n += 5
        turtle.pendown()
        turtle.colormode(255)
          
        a = random.randint(0, 255)
        b = random.randint(0, 255)
        c = random.randint(0, 255)
          
        # setting the outline 
        # and fill colour
        turtle.pencolor(a, b, c)
        turtle.fillcolor(a, b, c)
        turtle.begin_fill()
        turtle.fd(100)
        turtle.rt(90)
        turtle.fd(100)
        turtle.rt(90)
        turtle.fd(100)
        turtle.rt(90)
        turtle.fd(100)
        turtle.end_fill()
        turtle.penup()
        turtle.lt(angle)
    turtle.home()


def circle():
    turtle.clear()
    turtle.speed(50)

    angle = 30
    n = 5

    while n <= 200:
        n += 5
        turtle.pendown()
        turtle.colormode(255)
          
        a = random.randint(0, 255)
        b = random.randint(0, 255)
        c = random.randint(0, 255)
          
        # setting the outline 
        # and fill colour
        turtle.pencolor(a, b, c)
        turtle.fillcolor(a, b, c)

        turtle.begin_fill()
        turtle.circle(100)
        turtle.end_fill()
        turtle.penup()
        turtle.lt(angle)
    turtle.home()

def spiral():
    turtle.clear()
    turtle.speed(70)
    turtle.pensize(3)
    # turtle.pendown()
    n=5
    while n <= 100:
        turtle.circle(n)
        n = n+5
    turtle.penup()
    turtle.home()
    turtle.goto(80, 0)
    turtle.pendown()
    n=5
    while n <= 100:
        turtle.circle(n)
        n = n+5
    turtle.penup()
    turtle.home()
    turtle.penup()
    turtle.goto(120, -60)
    turtle.rt(90)
    turtle.pendown()
    n=5
    while n <= 100:
        turtle.circle(n)
        n = n+5
    turtle.penup()
    turtle.home()
    turtle.penup()
    turtle.goto(50, -40)
    turtle.lt(180)
    turtle.pendown()
    n=5
    while n <= 100:
        turtle.circle(n)
        n = n+5
    turtle.penup()
    turtle.home()

def triangle():
    turtle.clear()
    turtle.speed("fastest")
    turtle.pensize(1)
    turtle.pendown()
    for i in range(10,1150,9):
        turtle.fd(i)
        turtle.left(119.3)
    turtle.penup()
    turtle.home()


def octagon():
    turtle.clear()

    n = 5

    while n <= 379:
        n += 5
        turtle.pendown()
        turtle.colormode(255)
          
        a = random.randint(0, 255)
        b = random.randint(0, 255)
        c = random.randint(0, 255)
          
        # setting the outline 
        # and fill colour
        turtle.pencolor(a, b, c)
        turtle.fillcolor(a, b, c)
        turtle.begin_fill()
        for i in range(8):
            turtle.forward(100) 
            turtle.right(45)
        for j in range(8):
            turtle.forward(100) 
            turtle.right(45)
        turtle.rt(5)
        turtle.end_fill()

def wavey_tree():
    hue = 0.0
    for i in range(185):
        col = colorsys.hsv_to_rgb(hue,1,1)
        turtle.pencolor(col)
        hue += 0.005
        turtle.circle(190-i,100)
        turtle.lt(90)
        turtle.circle(190-i,100)
        turtle.rt(61)
    # turtle.hideturtle()


def flowerchild():
    turtle.clear()
    turtle.speed(10)
    turtle.pensize(2)
    turtle.color('red', 'yellow')
    turtle.begin_fill()
    turtle.pendown()
    while True:
        turtle.forward(200)
        turtle.left(170)
        if abs(turtle.pos()) < 1:
            break
    turtle.end_fill()
    turtle.penup()
    turtle.goto(-100, -100)
    turtle.lt(90)
    turtle.pendown()
    turtle.color('blue', 'light blue')
    turtle.begin_fill()
    for i in range(1, 37):
        turtle.forward(200)
        turtle.left(170)
    turtle.end_fill()
    turtle.penup()
    turtle.goto(100, -160)
    turtle.lt(90)
    turtle.pendown()
    turtle.color('purple', 'pink')
    turtle.begin_fill()
    for i in range(1, 37):
        turtle.forward(200)
        turtle.left(170)
    turtle.end_fill()
    turtle.penup()
    turtle.home()
    turtle.hideturtle()

