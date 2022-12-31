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
turtle.pensize(10)
turtle.pencolor("yellow")
# turtle = turtle.Turtle()

def direct_request(user_input):
    """
    Takes in the user answer as an instruction and directs the program to 
    execute that instruction.
    return: calls the necessary function to draw the shape or pattern.
    """

    if user_input == "Flower Child":
        bring_the_brightness = flowerchild()
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
        draw_million_stars = million_stars(360)
        return draw_million_stars
    elif user_input == "Exit":
        exit()
    

def star_spiral():
    turtle.clear()
    turtle.pensize(4)
    n = 30   
    x = 144   
    angle = 30 
    
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
    turtle.clear()
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


def circle():
    turtle.clear()
    turtle.begin_fill()
    turtle.circle(60)
    turtle.end_fill()
    turtle.home()

def spiral():
    turtle.clear()
    turtle.pensize(3)
    n=5
    while n <= 100:
        turtle.circle(n)
        n = n+5
    turtle.home()
    turtle.penup()
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
    turtle.begin_fill()
    turtle.rt(90)
    turtle.fd(100)
    turtle.lt(120)
    turtle.fd(100)
    turtle.lt(120)
    turtle.fd(100)
    turtle.end_fill()
    turtle.home()


def octagon():
    turtle.clear()
    turtle.begin_fill()
    for i in range(8):
        turtle.forward(100) 
        turtle.right(45) 
    turtle.end_fill()


def flowerchild():
    turtle.clear()
    turtle.pensize(2)
    turtle.color('red', 'yellow')
    turtle.begin_fill()
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
    turtle.goto(100, -100)
    turtle.lt(90)
    turtle.pendown()
    turtle.color('purple', 'pink')
    turtle.begin_fill()
    for i in range(1, 37):
        turtle.forward(200)
        turtle.left(170)
    turtle.end_fill()


def million_stars(size):
    turtle.clear()
    turtle.pensize(1)
    turtle.speed(10)
    turtle.color("red")

    turtle.penup()
    turtle.goto((-200, 50))
    turtle.pendown()
    while True:
        if size <= 10:
            return
        else:
            for i in range(5):
                # turtle.pendown()
                # moving turtle forward
                turtle.forward(size)
                million_stars(size/3)

                # moving turtle left
                turtle.left(216)
        break


def get_user_input(shape_patterns):
    """
    Will ask the user for input as to what shape or pattern they would like.
    param: shape: This is the list of valid shapes.
    param: patterns: A list of valid patterns that can be created.
    return: It will return a valid response from the user in Title Case.
    """
    while True:
        user_answer = input("What would you like your turtle to do?: ").title()
        user_answer_1 = user_answer.split()
        for i in user_answer_1:
            if (i.isalpha() == True) and (user_answer in shape_patterns):
                return user_answer
            elif user_answer.isnumeric or user_answer.isdigit() or user_answer == "":
                try_again = print("Invalid answer, please try again")
                return try_again


def display_options():
    """
    Displays the instructions to the game and shows the user all the valid
    commands that are acceptable.
    return: str: returns the program instructions in a string.
    """
    message_1 = str("""
    Hi There, 

    Welcome to our turtle park. We're so happy to have you.

    Here at "Tip-Top-Turtle Park", we enjoy seeing our turtles do all kinds of tricks and 
    flips. 

    - Press ENTER to proceed -

    """)
    return message_1

def get_first_response():
    """
    After the user has been shown initial shapes list then we need them to type
    continue to proceed with the program
    return: This function will return the first response from the user
    """
    
    while True:
        is_it_a_go = input("<Press Enter>")
        if is_it_a_go == "":
            return is_it_a_go
        else:
            not_right = str("Invalid response, please try again.")
            return not_right


def oh_wait_theres_more(shape_patterns):
    """
    Displays more options for turtle patterns.
    """

    message_2 = str("""
    Awesome! 

    Now let's get started with some shapes and patterns. Here's a list of all the
    cool things you can get your turtle to do on your screen.


    * Spiral                  * Flower Child          * Triangle
    * Star Spiral             * Square                * Octagon
    * Million Stars           * Circle

    Now try a few more shapes and patterns. When you want to quit the program, 
    type "Exit" when prompted.
    """)
    return message_2


def valid_shape_patterns():
    """
    Defines a list of acceptable shapes and patterns that the turtle can draw.
    Return: List: it should return a list of those shapes and patterns.
    """
    shapes = ["Square", "Circle", "Triangle", "Flower Child", "Star Spiral", "Spiral", "Octagon", "Million Stars", "Star Spiral"]
    return shapes


def welcome(shape_patterns):

    first_consent = get_first_response()
    if first_consent == "":
        print(oh_wait_theres_more(shape_patterns))
        answer = get_user_input(shape_patterns)
        direct_request(answer)
        return True


def draw_tings():
    """
    Runs the entire program from start to finish.
    """
    shape_patterns = valid_shape_patterns()
    print(display_options())
    wel = welcome(shape_patterns)
    while True:
        answer = get_user_input(shape_patterns)
        direct_request(answer)
            

if __name__=="__main__":
    draw_tings()