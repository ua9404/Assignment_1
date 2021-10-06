import turtle


def draw_shape_rectangle():
    turtle.up()
    turtle.goto(100, 100)
    turtle.down()
    turtle.fillcolor("red")
    turtle.begin_fill()
    turtle.forward(150)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(150)
    turtle.right(90)
    turtle.forward(100)
    turtle.end_fill()
    turtle.up()
    turtle.home()

def draw_shape_circle():
    turtle.up()
    turtle.goto(-100, -100)
    turtle.down()
    turtle.fillcolor("green")
    turtle.begin_fill()
    turtle.circle(50)
    turtle.end_fill()
    turtle.up()
    turtle.home()

def draw_shape_triangle():
    turtle.up()
    turtle.goto(50, 100)
    turtle.down()
    turtle.fillcolor("blue")
    turtle.begin_fill()
    turtle.right(60)
    turtle.forward(80)
    turtle.right(120)
    turtle.forward(80)
    turtle.right(120)
    turtle.forward(80)
    turtle.end_fill()
    turtle.done()


draw_shape_rectangle()
draw_shape_circle()
draw_shape_triangle()
