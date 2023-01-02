import turdle_works
# import million_stars


def direct_request(user_input):
    """
    Takes in the user answer as an instruction and directs the program to 
    execute that instruction.
    return: calls the necessary function to draw the shape or pattern.
    """

    if user_input == "Flower Child":
        bring_the_brightness = turdle_works.flowerchild()
        return bring_the_brightness
    elif user_input == "Square That":
        draw_square = turdle_works.square()
        return draw_square
    elif user_input == "Circle Swirl":
        draw_circle = turdle_works.circle()
        return draw_circle
    elif user_input == "Triangle":
        draw_triangle = turdle_works.triangle()
        return draw_triangle
    elif user_input == "Woven Basket":
        turdle_works.turtle.speed(300)
        draw_octagon = turdle_works.octagon()
        return draw_octagon
    elif user_input == "Spiral Cones":
        draw_spiral = turdle_works.spiral()
        return draw_spiral
    elif user_input == "Star Spiral":
        draw_star_spiral = turdle_works.star_spiral()
        return draw_star_spiral
    elif user_input == "Stary Night":
        turdle_works.turtle.clear()
        turdle_works.turtle.speed(70)
        turdle_works.turtle.pensize(2)
        turdle_works.turtle.penup()
        turdle_works.turtle.pendown()
        draw_million_stars = turdle_works.million_stars(250)
        return draw_million_stars
    elif user_input == "Exit":
        exit()


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
            elif user_answer.isnumeric or user_answer.isdigit() or user_answer \
            == "":
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

    Here at "Tip-Top-Turtle Park", we enjoy seeing our turtles do all kinds of \
    tricks and 
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


    * Spiral Cones            * Flower Child          * Triangle
    * Star Spiral             * Square That           * Woven Basket
    * Stary Night             * Circle Swirl

    Now try a few more shapes and patterns. When you want to quit the program, 
    type "Exit" when prompted.
    """)
    return message_2


def valid_shape_patterns():
    """
    Defines a list of acceptable shapes and patterns that the turtle can draw.
    Return: List: it should return a list of those shapes and patterns.
    """
    shapes = ["Square That", "Circle Swirl", "Triangle", "Flower Child", "Star Spiral", "Spiral Cones", "Woven Basket", "Stary Night", "Star Spiral"]
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
    welcome(shape_patterns)
    while True:
        answer = get_user_input(shape_patterns)
        direct_request(answer)
            

if __name__=="__main__":
    draw_tings()