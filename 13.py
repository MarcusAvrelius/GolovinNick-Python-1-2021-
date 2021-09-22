import turtle as tr

def circ(r):
    for i in range(360):
        tr.forward(r)
        tr.right(1)

tr.speed(10)
tr.fillcolor('yellow')
tr.begin_fill()
circ(2.5)
tr.end_fill()
tr.fillcolor('blue')
tr.penup()
tr.goto(-50,-40)
tr.pendown()
tr.begin_fill()
circ(0.5)
tr.end_fill()
tr.penup()
tr.goto(50,-40)
tr.pendown()
tr.begin_fill()
circ(0.5)
tr.end_fill()
tr.penup()
tr.goto(0,-75)
tr.width(3)
tr.pendown()
tr.goto(0,-150)
tr.penup()
tr.goto(-50,-200)
tr.color('red')
tr.pendown()
tr.right(90)
for i in range(180):
    tr.forward(0.9)
    tr.left(1)


