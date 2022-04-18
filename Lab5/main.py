import turtle
import math
import time

max_depth = int(input("\nEnter the fractal depth:"))

def fractal(aturt, depth, maxdepth):
    if depth > maxdepth:
        return

    length = 180*((math.sqrt(2)/2)**depth)
    anotherturt = aturt.clone()
    aturt.forward(length)
    aturt.left(45)
    fractal(aturt, depth+1, maxdepth)
    anotherturt.right(90)
    anotherturt.forward(length)
    anotherturt.left(90)
    anotherturt.forward(length)

    if depth != maxdepth:
        turtik = anotherturt.clone()
        turtik.left(45)
        turtik.forward(180*((math.sqrt(2)/2)**(1+depth)))
        turtik.right(90)
        fractal(turtik, depth+1, maxdepth)
    anotherturt.left(90)
    anotherturt.forward(length)


def draw_fractal():
    window = turtle.Screen()
    window.bgcolor('#AFEEEE')
    turtle.pencolor('#DC143C')
    turtle.pensize(3)
    turtle.hideturtle()
    #turtle.shape("circle")
    #turtle.resizemode("user")
    #turtle.shapesize(1, 1, 0)
    turtle.penup()
    turtle.goto(-75, -225)
    turtle.pendown()
    turtle.speed(100)
    turtle.left(90)
    fractal(turtle, 1, max_depth)
    print(f"\nВремя выполнения составило: {(time.time() - start_time) * 1000} миллисекунд")
    window.exitonclick()


start_time = time.time()
draw_fractal()
