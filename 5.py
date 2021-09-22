import turtle

for i in range(1,11):
    for j in range(4):
        turtle.forward(20 * i)
        turtle.right(90)
    turtle.left(90)
    turtle.penup()
    turtle.forward(10)
    turtle.left(90)
    turtle.forward(10)
    turtle.pendown()
    turtle.right(180)
    
