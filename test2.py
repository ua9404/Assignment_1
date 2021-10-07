import turtle
import drawings
import main

def test_goto():
    turtle.goto(60, 60)
    assert(turtle.xcor() == 60)
    assert(turtle.ycor() == 60)

def rectangle_will_fit():
    return True

def test_rectangle_will_fit(x, y, l, h):
    x = x.rectangle_will_fit(-200)
    assert (x == False)

    y = y.rectangle_will_fit(100)
    assert (y == False)

    l = l.rectangle_will_fit(-50)
    assert (l == True)

    h = h.rectangle_will_fit(50)
    assert (h == True)

def test_shape_rectangle(shape, x, y, color):
     s = shape("rectangle")
     assert (s == "rectangle")

     x = turtle.xcor(100)
     assert (x == 100)

     y = turtle.ycor(100)
     assert (y == 100)

     color = turtle.fillcolor("red")
     assert (color == "red")

def draw_shape_rectangle_perimeter(h, l):
    return (h+l+h+l)


def test_shape_rectangle_perimeter():
    x = draw_shape_rectangle_perimeter(100, 100)
    assert (x == 200)


def circle_will_fit(x, y, z):
    return True

def test_circle_will_fit(x=100):
    X = x.circle_will_fit
    assert (X == True)


def triangle_will_fit():
    return True

def test_triangle_will_fit(x, y, z):
    x = turtle.xcor(80)
    assert (x == 80)

    y = turtle.ycor(80)
    assert (y == 80)

    z = turtle.zcor(80)
    assert (z == 80)

def run_all_tests():
    test_goto()
    test_rectangle_will_fit()
    test_shape_rectangle()
    draw_shape_rectangle_perimeter()
    test_shape_rectangle_perimeter()
    test_circle_will_fit()
    test_triangle_will_fit()

run_all_tests()







