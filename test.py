import turtle


def triangle(length, depth):
    if depth == 0:
        return
    if depth ==1:
        tmp.begin_fill()
    for i in range(0,3):
        triangle(length/2, depth-1)
        tmp.forward(length)
        tmp.right(120)
    if depth ==1:
        tmp.end_fill()
    triangle(length/2, depth-1)


tmp = turtle.Turtle()
tmp.color('green','yellow')
tmp.shape('turtle')
tmp.fillcolor('red')
tmp.speed(150)
screen = turtle.Screen()

tmp.left(60)
triangle(300, 6)
screen.exitonclick()