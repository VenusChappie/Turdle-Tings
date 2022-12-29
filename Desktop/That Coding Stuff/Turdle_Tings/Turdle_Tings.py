import sys
import turtle
import random

screen = turtle.Screen()
screen.setup(500,500, startx = 50,
         starty = -200)
turtle.shape("turtle")
turtle.left(90)
turtle.bgcolor("black")
turtle.color("yellow", "orange")
turtle.title("turtle Tings Doing The Tings")
turtle.pensize(20)
turtle.pencolor("yellow")
# turtle = turtle.Turtle()

def direct_request(user_input):
    """
    Takes in the user answer as an instruction and directs the program to 
    execute that instruction.
    return: calls the necessary function to draw the shape or pattern.
    """

    if user_input == "Bright Star":
        bring_the_brightness = bright_star()
        return bring_the_brightness
    elif user_input == "Square":
        draw_square = square()
        return draw_square
    elif user_input == "Circle":
        draw_circle = circle()
        return draw_circle
    elif user_input == "Triangle":
        draw_triangle = triangle()
        return draw_triangle
    elif user_input == "Octagon":
        draw_octagon = octagon()
        return draw_octagon
    elif user_input == "Spiral":
        draw_spiral = spiral()
        return draw_spiral
    elif user_input == "Star Spiral":
        draw_star_spiral = star_spiral()
        return draw_star_spiral
    elif user_input == "Million Stars":
        draw_million_stars = million_stars()
        return draw_million_stars
    

def star_spiral():
    n = 30   
    x = 144   
    angle = 18 
    
    for i in range(n):
          
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
    

def square():
    turtle.begin_fill()
    turtle.fd(100)
    turtle.rt(90)
    turtle.fd(100)
    turtle.rt(90)
    turtle.fd(100)
    turtle.rt(90)
    turtle.fd(100)
    turtle.end_fill()
    turtle.home()

def smiley_face(col, rad):
    turtle.down()
    turtle.fillcolor(col)
    turtle.begin_fill()
    turtle.circle(rad)
    turtle.end_fill()
    turtle.up()
 
    # draw face
    turtle.fillcolor('yellow')
    turtle.begin_fill()
    turtle.circle(100)
    turtle.end_fill()
    turtle.up()
    
    # draw eyes
    turtle.goto(-40, 120)
    eye('white', 15)
    turtle.goto(-37, 125)
    eye('black', 5)
    turtle.goto(40, 120)
    eye('white', 15)
    turtle.goto(40, 125)
    eye('black', 5)
    
    # draw nose
    turtle.goto(0, 75)
    turtle.circle('black', 8)
    
    # draw mouth
    turtle.goto(-40, 85)
    turtle.down()
    turtle.right(90)
    turtle.circle(40, 180)
    turtle.up()
    
    # draw tongue
    turtle.goto(-10, 45)
    turtle.down()
    turtle.right(180)
    turtle.fillcolor('red')
    turtle.begin_fill()
    turtle.circle(10, 180)
    turtle.end_fill()
    turtle.hideturtle()

def circle():
    turtle.begin_fill()
    turtle.circle(60)
    turtle.end_fill()
    turtle.home()

def spiral():
    n=5
    while n <= 40:
        turtle.circle(n)
        n = n+5
    turtle.home()

def triangle():
    turtle.begin_fill()
    turtle.fd(100)
    turtle.lt(120)
    turtle.fd(100)
    turtle.lt(120)
    turtle.fd(100)
    turtle.end_fill()
    turtle.home()


def octagon():
    turtle.begin_fill()
    for i in range(8):
        turtle.forward(100) 
        turtle.right(45) 
    turtle.end_fill()

def bright_star():
    turtle.color('red', 'yellow')
    turtle.begin_fill()
    while True:
        turtle.forward(200)
        turtle.left(170)
        if abs(turtle.pos()) < 1:
            break
    turtle.end_fill()
    turtle.done()

def million_stars():
    stars = turtle.Turtle()
    size = 360
  
    # increases the speed of turtle
    stars.speed(10)
    
    # to change the background color
    stars.getscreen().bgcolor("black")
    stars.color("red")
    
    # stop drawing
    stars.penup()
    
    # move the turtle
    stars.goto((-200, 50))
    
    # start drawing
    stars.pendown()
    if size <= 10:
        return
    else:
        for i in range(5):
            
            # moving turtle forward
            turtle.forward(size)
            stars(turtle, size/3)
  
            # moving turtle left
            turtle.left(216)


def get_user_input(shape_patterns):
    """
    Will ask the user for input as to what shape or pattern they would like.
    param: shape: This is the list of valid shapes.
    param: patterns: A list of valid patterns that can be created.
    return: It will return a valid response from the user in Title Case.
    """
    while True:
        user_answer = input("What would you like your turtle to do?: ")
        if user_answer.isalpha() and user_answer in shape_patterns:
            return user_answer.title()
        elif user_answer.isnumeric or user_answer.isdigit() or user_answer == "":
            try_again = str("Invalid answer, please try again")
            print(try_again)


def display_options():
    """
    Displays the instructions to the game and shows the user all the valid
    commands that are acceptable.
    return: str: returns the program instructions in a string.
    """
    message_1 = str("""
    Hi There, 

    Welcome to our turtle park. We're so happy to have you.

    Here at "turtle park", we enjoy seeing our turtles do all kinds of tricks and 
    flips. 

    Try out some of them: 

    * Bright Star
    * Square
    * Circle
    * Triangle
    * Octagon

    Try one out for starters

    - Type 'Yes' or 'No' to proceed -
    """)
    return message_1

def get_first_response():
    """
    After the user has been shown initial shapes list then we need them to type
    continue to proceed with the program
    return: This function will return the first response from the user
    """
    
    while True:
        is_it_a_go = input("Would you like to proceed? Yes/No: ")
        if is_it_a_go == "Yes" or is_it_a_go == "No":
            return is_it_a_go
        else:
            not_right = str("Invalid response, please try again.")
            return not_right


def oh_wait_theres_more():
    """
    Displays more options for turtle patterns.
    """

    message_2 = str("""Awesome! 

    Now that you've tried one of our shapes, don't be shy, try out some of our 
    patterns available.

    * Spiral
    * Star Spiral
    * Million Stars

    Now try a few more shapes and patterns. When you want to quit the program, 
    type "Exit" when prompted.
    """)
    return message_2


def valid_shape_patterns():
    """
    Defines a list of acceptable shapes and patterns that the turtle can draw.
    Return: List: it should return a list of those shapes and patterns.
    """
    shapes = ["Square", "Circle", "Triangle", "Bright Star", "Star Spiral", "Octagon", 
    "Million Stars", "Star Spiral"]
    return shapes

def draw_tings():
    """
    Runs the entire program from start to finish.
    """
    print(display_options())
    first_consent = get_first_response()
    while first_consent:
        if first_consent == "No":
            break
        else:
            smiley_face("yellow", 300)
    oh_wait_theres_more()

if __name__=="__main__":
    draw_tings()