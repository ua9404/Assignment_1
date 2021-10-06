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
    turtle.done()



