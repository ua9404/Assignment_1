import turtle
import main

def test_goto():
    turtle.goto(60, 60)
    assert(turtle.xcor() == 60)
    assert(turtle.ycor() == 60)

def test_rectangle_will_fit(x, y, l, h):
    X = x.rectangle_will_fit(-200, 200, 100, 50)
    assert (X == False)

    X = y.rectangle_will_fit(100, 200, 50, 75)
    assert (X == False)

    X = l.rectangle_will_fit(-50, -250, 100, 200)
    assert (X == True)

    X = h.rectangle_will_fit(50, 200, 150, 75)
    assert (X == True)
