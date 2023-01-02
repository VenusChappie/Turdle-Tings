import random
import turtle

def million_stars(size):

	if size <= 10:
		return
	else:
		for i in range(5):
            turtle.colormode(255)
          
            a = random.randint(0, 255)
            b = random.randint(0, 255)
            c = random.randint(0, 255)
            
            # setting the outline 
            # and fill colour
            turtle.pencolor(a, b, c)
			turtle.forward(size)
			million_stars(size/3)
			turtle.left(216)