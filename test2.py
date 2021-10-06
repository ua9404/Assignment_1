import turtle
import main

def test_goto():
    turtle.goto(60, 60)
    assert(turtle.xcor() == 60)
    assert(turtle.ycor() == 60)

def test_rectangle_will_fit(x, y, l, h):
    x = x.rectangle_will_fit(-200)
    assert (x == False)

    y = y.rectangle_will_fit(100)
    assert (y == False)

    l = l.rectangle_will_fit(-50)
    assert (l == True)

    h = h.rectangle_will_fit(50)
    assert (h == True)

    test_goto()
    test_rectangle_will_fit()
