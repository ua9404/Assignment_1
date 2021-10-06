import turtle
import drawings
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
    return (h+l)


def test_shape_rectangle_perimeter(h, l):
    x = draw_shape_rectangle_perimeter(100, 100)
    assert (x == 200)

def run_all_tests():
    test_goto()
    test_rectangle_will_fit()
    test_shape_rectangle()
    draw_shape_rectangle_perimeter()
    test_shape_rectangle_perimeter()

run_all_tests()







